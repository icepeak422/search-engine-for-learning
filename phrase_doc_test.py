##this code can realize the function to extract doc_vector from doc in phrase and word
from __future__ import print_function
import numpy as np
import sys
import re


#build concept bag
conceptbag={'functions': 1, 'linear alegbra': 2, 'vector': 3,  'machine learning': 4, 'differential equations': 5}

#build the model of document
docs = open('phrase_test.txt').readlines()
# vectors=open("doc_vector.txt","w")
for line in docs:
	words=[]
	words_line = line.split()
	for i in range(0,len(words_line)):
		word = words_line[i]
		word = re.sub(r'[^a-zA-Z]+','', word)
		word = word.lower()
		if word!='':
			words.append(word)
	print(words)

	doc_vec=np.zeros(5)
	for i in range(0,len(words)):
		word = words[i]
		if word in conceptbag:
			doc_vec[conceptbag[word]-1]+=1
		if(i<len(words)-1):
			word = words[i]+' '+words[i+1]
			if word in conceptbag:
				doc_vec[conceptbag[word]-1]+=1
	# doc_wordcount[num]= doc_vec
	print(doc_vec)

