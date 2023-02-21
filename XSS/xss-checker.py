#!/usr/bin/python3

from requests import (
    get,
    post,
    Session
)


class XSSChecker:
    def __init__(self, url:str = None) -> None:
        self.url = url
        self.payload = None
        self.sess = Session()
        
        
    def checking_fields_to_inject(self):
        pass
        
    
    def _send_attack(self, payload=None):
        if payload is None:
            simple_payload = """<script>alert('xss')</script>"""
        pass

    def send_data(self):
        response = post(url=self.url, )


def main():
    pass


if __name__ == "__main__":
    main()
