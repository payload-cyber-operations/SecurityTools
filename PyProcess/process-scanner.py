#!/usr/bin/python3

import os
import subprocess
import logging



def check_network_process():
    """probbly one of the most beautiful scripts
    about the connections networking.
    """
    pass




def checking_process(status_value: str) -> None:
    process = subprocess.Popen([f"systemctl list-units --type=service --state={status_value}"],
                               stdout=subprocess.PIPE, shell=True)

    out, err = process.communicate()
    decode_regular = out.decode().replace('\n', '\n')
    print(decode_regular)
    for line in out.decode().split('\n'):
        columns = line.split()
        if columns:
            if columns[2].lower() == "active":
                print(columns[0])
        else:
            continue



def main():
    # checking_process(status_value="running")
    check_network_process()

if __name__ == "__main__":
    main()
