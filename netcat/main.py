#!/usr/bin/python

import requests
from pprint import pprint
import json


def main():
    try:
        data = {"name": "Arturo"}
        headers = {'Content-Type': "application/json"}
        res = requests.post("https://webhook.site/4ed54cff-41ba-423e-9f46-b2c87408daf9",
                data=json.dumps(data), headers = headers)
        pprint(res.text)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
