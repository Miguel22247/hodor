#!/usr/bin/python3


"""Hodor my Holberton ID 1024 times."""
import requests
import time

payload = {'id': '2780', 'holdthedoor': 'Submit'}
failed = 0

for i in range(0, 1024):
    request = requests.post("https://158.69.76.135/level0.php", data=payload)
    if request.status_code != 200:
        print("failed to post {}th request".format(i))
        failed += 1

print("Failed {} number of times".format(failed))
