import re
import requests
from bs4 import BeautifulSoup 
from urllib import urlopen
import numpy as np
from pdf_test import pdf2txt

#url_res = np.load('url_res.npy')


conceptbag = np.load('../bag/new_conceptbag.npy').item()
def url_extract(urls):
	vecs=[]
	tuples={}
	for p in range(0,len(urls)):
		text=''
		vecs.append(np.zeros(192))
		url=urls[p]
		r = requests.get(url)
		content_type = r.headers.get('content-type')
		print(url)
		if("youtube" not in url):
			if("springer" not in url):
				if("package" not in url):
					if("http://reference.wolfram.com/" not in url):
						if("www.udacity.com" not in url):
							if("www.symbolab.com" not in url):
								if("eigen.tuxfamily.org" not in url):
									if("www.emathhelp.net" not in url):
										if("amazon" not in url):
											if("www.mathworks.com" not in url):
												if("www.osapublishing.org" not in url):
													if("http://www.dummies.com/" not in url):
														if 'application/pdf' in content_type:
															text =pdf2txt(url)
														elif 'text/html' in content_type:
															# html = urlopen(url).read()
															# soup = BeautifulSoup(html,"lxml")    
															# text = soup.get_text()
															text = r.text
		docs = text
		# vectors=open("doc_vector.txt","w")
		words=[]
		words_line = docs.split()
		for i in range(0,len(words_line)):
			word = words_line[i]
			word = re.sub(r'[^a-zA-Z-]+','', word)
			word = word.lower()
			if word!='':
				words.append(word)

		for i in range(0,len(words)):
			word = words[i]
			if word in conceptbag:
				print(word)
				vecs[p][conceptbag[word]-1]+=1
			if(i<len(words)-1):
				word = words[i]+' '+words[i+1]
				if word in conceptbag:
					print(word)
					vecs[p][conceptbag[word]-1]+=1
			if(i<len(words)-2):
				word = words[i]+' '+words[i+1]+' '+words[i+2]
				if word in conceptbag:
					print(word)
					vecs[p][conceptbag[word]-1]+=1
		# doc_wordcount[num]= doc_vec
		# print(p)
		# print(vecs[p])
		tuples[p]= vecs[p]
	return tuples
