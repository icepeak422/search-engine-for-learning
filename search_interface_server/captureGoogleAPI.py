#!C:/Python27/python.exe
import cgi, cgitb, sys
import requests
import urllib, urllib3
from bs4 import BeautifulSoup, SoupStrainer
import types
import os
import json

#cgitb.enable()


basePath = os.path.dirname(os.path.realpath(__file__))+"\\"



# protects against invalid unicode characters
def rectify(selstr):
	val = ''.join([x for x in selstr if ord(x)<128])
	return str(val)


	


	

def formatSnippet(snipstr):
	if (snipstr[-3:]=="..."):
		snipstr = snipstr[:-3]
	snipstr = snipstr.replace("  "," ")
	snipstr = snipstr.replace("   ", " ")
	return snipstr
	


# modified: startIndex error. MUST start at 1 at minimum. resolved
def fetchRecords(userquery, startIndex=1):
	liveMode = True
	if startIndex%10==0:
		startIndex = startIndex + 1 # API thing

	if liveMode==True:
		apikey = "AIzaSyAGw6MwyZe-H68Kt3vIeOk9T3620g0aRVY"
		#apikey = "AIzaSyD13KEY4zNRONAR4vR0eL0YmqvT1eI7Cv4" # this is my key
		# fetch the data from the API
		selquery = urllib.quote_plus(userquery)
		# &searchType=image
		selurl = "https://www.googleapis.com/customsearch/v1?key="+apikey+"&cx=007865715089351041060:znf9injp6vi&q="+selquery+"&num=10&start="+str(startIndex)
		

		# we now have the JSON results
		ch = requests.get(selurl)
		res = rectify(ch.text)
		jstr = res
		jstruct = json.loads(res)
		
		# store the raw results
		handle = open(basePath+"apires.json", "w")
		handle.write(res)
		handle.close()
		
	else:
		# retrieve the data from our source document
		handle = open(basePath+"apires.json", "r")
		jstr = rectify(handle.read())
		jstruct = json.loads(jstr)
		handle.close()
		
	
	allresults = []

	# begin processing
	print "BEGIN:"+str(startIndex)+":"+userquery
	for i in range(0,len(jstruct["items"])):
		linkRef = jstruct["items"][i]["link"]
		linkTitle = jstruct["items"][i]["title"]
		linkSnippet = jstruct["items"][i]["snippet"]
		linkAge = 1
		linkSize = 1
		allresults.append({"title":linkTitle, "link":linkRef, "snippet":linkSnippet, "age":linkAge, "size":linkSize})
			
	return allresults
	
	



