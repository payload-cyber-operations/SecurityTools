#!/usr/bin/python3

import subprocess
import re

"""
    @author Arturo Negreiros Samanez
"""


class Fetching:

    def __init__(self):
        pass

    @staticmethod
    def get_ttl(address):

        process = subprocess.Popen(["ping -c 1 %s " % address, ""], stdout=subprocess.PIPE, shell=True)
        out, err = process.communicate()
        out = out.decode("utf-8")
        out = out.split()
        # print(out[12])
        out = re.findall(r"\d{1,3}", out[12])
        # print(out[0])

        if err is not None:
            return out[0]
        else:
            return err

    @staticmethod
    def get_os(ttl: int) -> str:

        if 0 <= ttl <= 64:
            return "Linux machine"

        elif 65 <= ttl <= 128:
            return "Box Windows"

        else:
            return "Unknown"


def main():
    pass


if __name__ == "__main__":
    main()
