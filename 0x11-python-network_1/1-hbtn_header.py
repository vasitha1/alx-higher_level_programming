#!/usr/bin/python3
"""
Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""


import urllib.request
import sys


def main():
    URL = sys.argv[1]
    request = urllib.request.Request(URL)
    with urllib.request.urlopen(request) as response:
        # Read the response content
        html = response.read()

        # Get the X-Request-Id from the response headers
        request_id = response.getheader('X-Request-Id')

        print('{}'.format(request_id))

if __name__ == "__main__":
    main()
