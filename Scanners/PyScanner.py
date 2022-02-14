#!/usr/bin/python3

import socket
import sys
import getopt
import os
from IPy import IP


class Socket_connection:

    def __init__(self, host_, port_):
        self.sock = None
        self.port = port_
        self.host = host_
        self.host_name = None
        self.connect = None
        self.address = None

    def socket_create(self):
        """Create the connection for the sockets"""
        try:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error as error:
            print("Error creating socket by: ",str(error))


    def socket_bind(self):

        try:
            self.sock.bind((str(self.host), int(self.port)))
            self.sock.listen(1)
            print("[*] Connection stablished...")
        except Exception as e:
            print("Socket binding error: ", str(e))
            self.socket_bind()
            
    def socket_accept_connection(self):

        try:
            self.connect, self.addrress = self.sock.accept()
            print("[*] Session opened at %s %s"%(self.addrress[0], self.addrress[1]))
            print("\n")
            self.host_name = self.connect.recv(1024)
        except socket.error as err:
            print("Error getting the connection: ", str(err))

payload = ''
path = "/usr/bin/bash" # path to reverse shell
stack = list()
info = False
port = 0
host = ''
reverse = False



def global_variables():
    global payload
    global path
    global stack
    global info
    global port
    global host
    global reverse

    
# initializr this funciton to get the global variables in whole the code.
global_variables()




# this will be contain the value for use on bufferoverflow

def check_ip(ip):

    try:
        IP(ip)
        return ip
    except:
        return socket.gethostbyname(ip)

def showing():

    print("This command line shell is for try to get reverse shell from METASPLOITABLE")
    print("""\n
    -s --scanning           is for general scanner from the ip, getting the ports currently open
    -r --reverse            if puting a host target and especific port to try to get reverse shell""")



def show_port_opened(host, name_port):
    """The purpose is get and discover which port is opened"""

    host_name = check_ip(host)

    try:

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            sock.connect((host_name, name_port))
            port_name = socket.getnameinfo((str(host), name_port), socket.NI_NUMERICHOST)
            print("port %s  port name %s"%(name_port, port_name))
        except Exception:
            return None

        return port
    except:
        return None


def reverse_shell(host,port):
    pass


def init_process():

    try:
        opts, args = getopt.getopt(sys.argv[1:], "is:g:rp:h:", ["info","scanning=", "general=", 
            "reverse", "port=", "host="])
        for o,a in opts:
            
            if o in ('-s','--scanning'):
                print("[*] Listing the open ports")
                for x in range(1,1000):
                    show_port_opened(a, x)
                exit()
            elif o in ('-g','--general'):
                pass

            elif o in ('-i','--info'): showing()

            elif o in ('-r','--reverse'):reverse = True
                
            elif o in ('-p','--port'): port = int(a)

            elif o in ('-h','--host'): host = str(a)

        if reverse:

            try:
                print(host)
                print(port)
                if port is not None and host is not None:
                    sock = Socket_connection(host, port)
                    sock.socket_create()
                    sock.socket_bind()
                    sock.socket_accept_connection()
                    
                else:
                    showing()
                
            except Exception as e:
                print("error: ",str(e))
            exit()

    except Exception as e:
        print("Error by: ", str(e))





if __name__ == '__main__':

    init_process()
