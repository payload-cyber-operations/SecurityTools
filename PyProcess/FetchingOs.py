#!/usr/bin/python3

import subprocess
import re
import inspect


"""
    @author Arturo Negreiros Samanez
"""


class Fetching:

    def __init__(self):
        pass
    

    def get_ttl(self, address):

        process = subprocess.Popen(["ping -c 1 %s "%address, ""], stdout = subprocess.PIPE, shell = True)
        out, err = process.communicate()
        out = out.decode("utf-8")
        out = out.split()
        #print(out[12])
        out = re.findall(r"\d{1,3}", out[12])
        #print(out[0])

        if err is None:
            return out[0]
        else:
            return err


    def get_os(self, ttl:int)-> str: 

        if ttl >= 0 and ttl <= 64:
            return "Linux machine"

        elif ttl >= 65 and ttl<=128:
            return "Box Windows"

        else:
            return "Unknown"
        

def wherever(name_list:list, name: str, age:int, salary:float) -> bool:

    return "hello"


def main():
    pass


if __name__ == "__main__":
    main()