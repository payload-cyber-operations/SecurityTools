#!/usr/bin/python3

import subprocess
import shlex
import argparse
import socket
import threading
import sys
import textwrap




def execute(cmd: str):
    cmd = cmd.strip()
    if not cmd:
        return
    process = subprocess.check_output(shlex.split(cmd), 
                            stderr=subprocess.STDOUT)
    return process.decode()



class NetCat:

    def __init__(self, args, buffer=None):
        self.args = args
        self.buffer = buffer
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def run(self):
        
        if self.args.listen:
            self._listen()
        else:
            self._send()
    

    def _send(self):
        self.socket.connect((self.args.target, self.args.port))
        if self.buffer:
            self.socket.send(self.buffer)

        try:

            while True:
                recv_len = 1
                response = ''

                while recv_len:

                    data = self.socket.recv(4096)
                    recv_len = len(data)
                    response += data.decode()
                    
                    if recv_len < 4096:
                        break
                        
                if response:
                    print(response)
                    buffer = input("> ")
                    buffer += '\n'
                    self.socket.send(buffer.encode())
        except KeyboardInterrupt:
            print("[!] Exiting...")
            self.socket.close()
            sys.exit()
            

    def _handle(self, sock: socket.socket):
        
        if self.args.execute:
            output = execute(self.args.execute)
            sock.send(output.encode())

        elif self.args.upload:
            file_buffer = b''

            while True:

                data = sock.recv(4096)
                if data:
                    file_buffer += data
                else:
                    break
            
            with open(self.args.upload, "wb") as file:
                file.write(file_buffer)
            
            message = f"saved file {self.args.upload}"
            sock.send(message.encode())
        
        elif self.args.command:
            cmd_buffer = b''
            while True:
                try:
                    sock.send(b'NETCAT #> ')

                    while '\n' not in cmd_buffer.decode():
                        cmd_buffer += sock.recv(64)
                    
                    response = execute(cmd_buffer.decode())

                    if response:
                        sock.send(response.encode())
                    cmd_buffer = b''
                except Exception as e:
                    print(f"Error by {e}")
                    self.socket.close()
                    sys.exit()



    def _listen(self):
        self.socket.bind((self.args.target, self.args.port))
        self.socket.listen(5)

        while True:
            client_socket, _ = self.socket.accept()
            client_thread = threading.Thread(target=self._handle, args=(client_socket,))
            client_thread.start()





def main():
    print("""
    '##::: ##:'########:'########::'######:::::'###::::'########:
     ###:: ##: ##.....::... ##..::'##... ##:::'## ##:::... ##..::
     ####: ##: ##:::::::::: ##:::: ##:::..:::'##:. ##::::: ##::::
     ## ## ##: ######:::::: ##:::: ##:::::::'##:::. ##:::: ##::::
     ##. ####: ##...::::::: ##:::: ##::::::: #########:::: ##::::
     ##:. ###: ##:::::::::: ##:::: ##::: ##: ##.... ##:::: ##::::
     ##::. ##: ########:::: ##::::. ######:: ##:::: ##:::: ##::::
    ..::::..::........:::::..::::::......:::..:::::..:::::..:::::

    '########::'#######:::'#######::'##:::::::
    ... ##..::'##.... ##:'##.... ##: ##:::::::
    ::: ##:::: ##:::: ##: ##:::: ##: ##:::::::
    ::: ##:::: ##:::: ##: ##:::: ##: ##:::::::
    ::: ##:::: ##:::: ##: ##:::: ##: ##:::::::
    ::: ##:::: ##:::: ##: ##:::: ##: ##:::::::
    ::: ##::::. #######::. #######:: ########:
    :::..::::::.......::::.......:::........::

    """)
    try:
        parser = argparse.ArgumentParser(
            description="Simple Netcat tool",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            epilog=textwrap.dedent('''Example:

                ./netcat -t 192.168.100.5 -p 5555 -l -c # command shell
                ./netcat -t 192.168.100.5 -p 5555 -l -u=myfile.txt # upload file
                ./netcat -t 192.168.100.5 -p 5555 -l -e=\"cat /etc/passwd" # execute command
                echo 'ABC' | ./netcat -t 192.168.100.5 -p 135 # echo text to server port 135
                ./netcat -t 192.168.100.5 -p 5555 -l -c 
            ''')
        )
        parser.add_argument('-c', '--command', action="store_true",help="command shell")
        parser.add_argument('-e', '--execute', help="execute specified command")
        parser.add_argument('-l', '--listen',action="store_true", help="make listening on specific port")
        parser.add_argument('-p', '--port', type=int, default=5555, help="specified port")
        parser.add_argument('-t', '--target', help="specified ip")
        parser.add_argument('-u', '--upload', help="upload file")

        args = parser.parse_args()

        if args.listen:
            buffer = ''
        else:
            buffer = sys.stdin.read()

        nc = NetCat(args, buffer.encode())
        nc.run()
    except KeyboardInterrupt:
        print("[!] Exiting")
        sys.exit()


if __name__ == "__main__":
    main()
    