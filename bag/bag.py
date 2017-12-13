from __future__ import print_function
import sys
import re
import numpy as np



#build the stopwords set
stopwords_lines = open('stopwords.txt').readlines()
stopwords = set()
for line in stopwords_lines:
	stop_word=line.strip('\t\n')
	stopwords.add(stop_word)


doc = open('new_conceptbag.txt').readlines()
conceptbag= {}
num=1
for line in doc:
	word = line.split('/n')[0]
	word = re.sub(r'[^a-zA-Z0-9 -]+','', word)
	if word != '':
		word = word.lower()
		if word not in conceptbag:
			conceptbag[word]= num
			num=num+1

print (num)
np.save('new_conceptbag.npy',conceptbag)
bag2=open("new_conceptbag2.txt","w")
print (conceptbag,file = bag2) 
sd=sorted(conceptbag.items())
print()