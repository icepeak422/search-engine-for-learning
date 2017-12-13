import os
import requests


def pdf2txt(url):
	response = requests.get(url)
	with open('metadata.pdf', 'wb') as f:
	    f.write(response.content)
	os.system("pdf2txt.py -o output.txt metadata.pdf")
	file = open('output.txt','r')
	text = file.read()
	os.system("rm output.txt")
	return text