#!/usr/bin/python
from __future__ import print_function
import numpy as np
import sys
import re


#build concept bag
conceptbag = np.load('conceptbag.npy').item()


#build the model of document
docs = open('docstest.txt').readlines()
doc_wordcount={}
num=0
vectors=open("doc_vector.txt","w")
for line in docs:
	wordcount={}
	doc_vec=np.zeros(369)
	words_line = line.split()
	for word in words_line:
		word = re.sub(r'[^a-zA-Z]+','', word)
		print(word)
		if word != '':
			word = word.lower()
			if word in conceptbag:
				# if conceptbag[word] not in wordcount:
				# 	wordcount[conceptbag[word]] = 1
				# else:
				# 	wordcount[conceptbag[word]] += 1
				doc_vec[conceptbag[word]-1]+=1

	# sd=sorted(wordcount.items());
	doc_wordcount[num]= doc_vec
	print(doc_vec, file = vectors)
	print("\n")
	num=num+1

np.save('doc_vector.npy',conceptbag)

print (np.dot(doc_wordcount[0], doc_wordcount[1]))

 
		

