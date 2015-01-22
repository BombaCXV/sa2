#!/usr/bin/env python

#University of Heidelberg
#Institute of Computational Linguistics
#Designing Experiments for Machine Learning Tasks
#Project Sentiment Analysis 2
#Dominik Both, Denis Orechov
#2014-2015

#This scripts converts the sentiment dictionary of the Standford Sentiment Bank into one JSON-Dictionary

#Init
import re, json, timeit
start = timeit.default_timer()
l = {}
l2 = {}
r = {}
#Should the dictionary also include phrases or only unigrams?
polygrams = True

#Open the dictionary, which consists of an ID and the phrase, separated by a pipe, each lemma separated by a line break. 
#The ID refers to another file which consists of the ID and the sentiment label of the referred lemma. Separation same as above.
with open("ext/sentimentbank/dictionary.txt") as fileobject:
    for line in fileobject:
		lines = line.split("|")
		#If only unigrams should be included, the regular expression filters all lemmas that include whitespace or other parting characters
		if re.match("^[A-Za-z']*$", lines[0]) or polygrams:
			l[lines[1].strip()] = lines[0]
#Now we got the dictionary l, mapping ID -> lemma
#Opening the sentiment label file, as stated above.
with open("ext/sentimentbank/sentiment_labels.txt") as fileobject:
    for line in fileobject:
		lines = line.split("|")
		try:
			#First line of file is a comment, which can't be parsed to float, thus except here. Another way would be filtering the first line.
			raw_st = float(lines[1].strip())
			sentiment = raw_st
			l2[lines[0].strip()] = sentiment
		except:
			print "Line ignored"
#So we got two dictionaries. l: ID->lemma and l2: ID->sentiment. We now merge them.
for key in l:
	r[l[key]] = l2[key]
#Save the produced dictionary as json
f = open("data/dictionary.json","w")
f.write(json.dumps(r))
f.close()
stop = timeit.default_timer()
print "Done. Dictionary contains "+str(len(r))+" items. Calculated in "+str(stop - start) +" seconds."