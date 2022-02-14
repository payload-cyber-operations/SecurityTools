
import socket
import sys
import getopt
import os
import time
import subprocess
from threading import *
from termcolor import colored
class Socket_connection:

    def __init__(self, host_, port_):
        self.sock = None
        self.host = host_
        self.port = port_
        self.host_name = None
        self.connect = None
        self.address = None
        self.message = None
        self.port_list_open = list()

    def socket_create(self):
        """Create the connection for the sockets"""
        try:
            #self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock = socket.socket()
        except socket.error as error:
            print("Error creating socket by: ",str(error))


    def socket_bind(self):
        # self.list_ports_openeds()
        try:
            socket_connect = sock.connect((str(self.host), int(self.port)))
            banner = socket_connect.recv(1024)
            port_info = colored("[+] {port} open".format(port=self.port),"green")
            banner = str(banner).replace("b'", "")
            print(port_info+"\t"+banner)
        except Exception as e:
            print(str(e))
        # try:
            
        #     """Getting the connection to server, in this case the server is VM Metasploitable"""
        #     try:
        #         for x in list_ports_openeds:
        #             self.sock.connect((str(self.host), int(x)))
        #             print("[*] Connection stablished...")

        #     except socket.error as e:
        #         print("Can't be possible connect with the host")
        # except Exception as e:
        #     print("Socket binding error: ", str(e))
        #     #self.socket_bind()
            
    def socket_accept_connection(self):

        try:
            self.connect, self.address = self.sock.accept()
            print(self.connect, self.address)
            print("\n")
            self.host_name = self.connect.recv(1024)
        except socket.error as err:
            print("Error getting the connection: ", str(err))
    

    def list_ports_openeds(self):

        def _create_internal_connection(host, port):
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((host, port))
                self.port_list_open.append(port)
                print("[*] Port %s open %s "%(port, socket.getnameinfo((self.host, port), socket.NI_NUMERICHOST)))
            except:
                pass
        try:
            print("[*] Trying to connect at %s ..."%self.host)
            print("")
            time.sleep(2)
            for x in range(1000):
                _create_internal_connection(self.host, x)
                
        except socket.error as error:
            print("Error by: ",str(error))

        
if __name__ == '__main__':
    
    #sock.socket_create()
    for x in range(1,1000):
        sock = Socket_connection("192.168.100.209", x)
        sock.socket_bind()


   

