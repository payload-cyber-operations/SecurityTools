#!/usr/bin/python3

"""
    simple tool to get in the clipboard
    the capture of the ports early stored
    in a simple file when you executed the 
    scanning with nmap and creating a -oG file

    :author: Arturo Negreiros aka HackThur
"""

import os
import sys
import re
import subprocess

def main():

    try:
        with open(sys.argv[1], "r") as file:
            data = file.read()

        allport = re.findall(r'\d{1,5}/open', data)
        ports = [re.search(r'\d{1,5}', x).group() for x in allport]
        ports = ",".join(ports)
        subprocess.Popen(f"echo {ports} | tr -d '\n' | xclip -sel clip", stdout=subprocess.PIPE, shell=True)
        print(f"\n[*] Ports in the clipboard {ports}")
        print(f"\n[*] Deleting  file {sys.argv[1]}")
        exit(0)

    except Exception:
        print("""
        \n\n\t [*] python3 extractPorts.py <grepable file>\n\n
              """)
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[!] Exiting...")


if __name__ == "__main__":
    main()
