#!/usr/bin/python3
 
 
"""hodor for level 0"""
import requests

page = "http://158.69.76.135/level0.php"
payloader = {'id': '2780', 'holdthedoor': 'Enviar'}

for i in range (0, 1024):
    payloader = requests.post(page, data = payloader)
    print("vote n* {:d} send it with code: {}".format(i, payloader))
