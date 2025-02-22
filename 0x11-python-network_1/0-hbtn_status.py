#!/usr/bin/python3
"""
This scrip fetches https://alx-intranet.hbtn.io/status
"""

import urllib.request


def main():
    with urllib.request.urlopen(
            'https://alx-intranet.hbtn.io/status'
    ) as response:
        html = response.read()

        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))


if __name__ == "__main__":
    main()
