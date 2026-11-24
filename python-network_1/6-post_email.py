#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request with the email
and displays the body of the response."""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}
    response = requests.post(url, data=data)
    print(response.text)
