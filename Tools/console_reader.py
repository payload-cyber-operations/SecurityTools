#!/usr/bin/python3

import time
import sys

def main():
    with open("console.log", "r") as f:
        for line in f:
            print(line, end="")

        while True:
            try:
                line = f.readline()

                if line:
                    print(line, end="")
                else:
                    time.sleep(1)
            except KeyboardInterrupt:
                print("[*] Exiting!!")
                break

if __name__ == "__main__":
        main()
