import scipy.io as sio
import numpy as np
import re
from score_2_doc import score_2_doc
from captureGoogleAPI import fetchRecords
from url_extract import url_extract


conceptbag = np.load('../bag/new_conceptbag.npy').item()

def recommend5url(urls):
	tuples=url_extract(urls)
	def numpos(vec):
		num=0
		for i in vec:
			if(i>0): num=num+1
		return num
	new_tuples=sorted(tuples.items(), key=lambda x: np.linalg.norm(x[1]), reverse = True)
	#print(new_tuples)

	for i in range(0,5):
		index = new_tuples[i][0]
		#print(index)
		#print urls[index]



	#calculate the score matrix
	scores=np.zeros((5,5))
	for i in range(0,5):
		for j in range(i+1,5):
			vec1 = new_tuples[i][1]
			vec2 = new_tuples[j][1]
			# v1 = np.linalg.norm(vec1)
			# vec1 = np.divide(vec1,v1)
			# v2 = np.linalg.norm(vec2)
			# vec2 = np.divide(vec2,v2)

			scores[i][j]= score_2_doc(vec1,vec2)
			scores[j][i]= - scores[i][j]
			# print(new_tuples[i][0])
	print (scores)

	ret={}
	for i in range(0,5):
		ret[i] = scores[i]


	ret=sorted(ret.items(), key=lambda x: numpos(x[1]), reverse = True)

	# find the reason word
	reasonwords={}
	simplewords=[]
	for i in range(0,5):
		url = urls[new_tuples[ret[i][0]][0]]
		wordvec = new_tuples[ret[i][0]][1]
		reasonwords[url]=[]
		for p in range(0,len(wordvec)):
			if(wordvec[p]>2):
				#p= argmax(wordvec)
				for key, value in conceptbag.iteritems():
					if(value == p+1):
						if(key not in simplewords):
							#print("reasonwhy_____"+key)
							reasonwords[url].append(key)
						simplewords.append(key)
		if(len(reasonwords[url])==0):
			reasonwords[url].append("similar concepts with previous document")

	# return the result 
	ret5ulrs=[]
	reasonret=[]
	for retitem in ret:
		vec = new_tuples[retitem[0]][1]
		if(np.linalg.norm(vec)==0):
			continue
		url = urls[new_tuples[retitem[0]][0]]
		print(url)
		ret5ulrs.append(url)
		reasonret.append(reasonwords[url])
		print(reasonwords[url])
	return ret5ulrs, reasonret


def recommend2start(ret):
	print('\033[1m' + "Do you want me to recommend where you should start? ")
	print '\033[0m'

	k = raw_input('> ')
	if k == 'Y':
		print('\033[1m' + "Ok, please answer some question...")
		print '\033[0m'
	if k== 'N':
		print('\033[1m' + "Bye..")
		print '\033[0m'
		quit()
	wordlist=[]
	for retitem in ret:
		# print(urls[new_tuples[retitem[0]][0]])
		# print (new_tuples[retitem[0]][0])
		for p in range(0,len(new_tuples[retitem[0]][1])):
			if(new_tuples[retitem[0]][1][p]>0):
				if conceptbag.keys()[conceptbag.values().index(p+1)] not in wordlist:
					print('\033[1m' + "are you familiar with " + conceptbag.keys()[conceptbag.values().index(p+1)] + "?")
					print '\033[0m'
					k = raw_input('> ')
					if k == 'Y':
						wordlist.append(conceptbag.keys()[conceptbag.values().index(p+1)])
						continue
					if k== 'N':
						print('\033[1m' + "we recommend you read from:" + urls[new_tuples[retitem[0]][0]])
						print '\033[0m'
						quit()
	



