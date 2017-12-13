#!/usr/bin/python
from __future__ import print_function
import numpy as np
import sys
import re


#build concept bag
conceptbag = np.load('new_conceptbag.npy').item()


#build the model of document
docs = open('umichmath.txt').readlines()
course_wordcount={}
num=0
vectors=open("course_vector.txt","w")
for line in docs:
	words=[]
	words_line = line.split()
	for i in range(0,len(words_line)):
		word = words_line[i]
		word = re.sub(r'[^a-zA-Z-]+','', word)
		word = word.lower()
		if word!='':
			words.append(word)
	
	wordcount={}
	for i in range(0,len(words)):
		word = words[i]
		if word in conceptbag:
			if conceptbag[word] in wordcount:
				wordcount[conceptbag[word]]+=1
			else:
				wordcount[conceptbag[word]]=1
		if(i<len(words)-1):
			word = words[i]+' '+words[i+1]
			if word in conceptbag:
				if conceptbag[word] in wordcount:
					wordcount[conceptbag[word]]+=1
				else:
					wordcount[conceptbag[word]]=1
		if(i<len(words)-2):
			word = words[i]+' '+words[i+1]+' '+words[i+2]
			if word in conceptbag:
				if conceptbag[word] in wordcount:
					wordcount[conceptbag[word]]+=1
				else:
					wordcount[conceptbag[word]]=1

	sd=sorted(wordcount.items());
	course_wordcount[num]= sd
	print(sd, file = vectors)
	print("\n")
	num=num+1

np.save('course_vector.npy',course_wordcount)


 
		

