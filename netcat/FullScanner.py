#!/usr/bin/python3

"""
:author Arturo Payload
"""
import socket
import sys

ports = range(1, 65536)


def main():

    for port in ports:
        try:
            if len(sys.argv) != 2:
                print("[*] Put a ip address after the name of this file and before enter xD")
                sys.exit(1)
            scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            scanner.connect((sys.argv[1], port))
            service_name = socket.getnameinfo((sys.argv[1], port), socket.NI_NUMERICHOST)
            print("service {} at port {} openened".format(service_name, port))
        except Exception:
            pass
        except KeyboardInterrupt:
            print("[!] Exiting...")
            sys.exit(1)


if __name__ == "__main__":
    main()



