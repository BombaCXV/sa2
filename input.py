#!/usr/bin/env python

#University of Heidelberg
#Institute of Computational Linguistics
#Designing Experiments for Machine Learning Tasks
#Project Sentiment Analysis 2
#Dominik Both, Denis Orechov
#2014-2015

#on the fly average classifier. using average of words in dictionary. to get out of the loop type type quit as sentence

import json
#load dictionary
json_data2 = open("data/dictionary.json").read()
dict = json.loads(json_data2)
#allow to classify an infinite amount of sentences..
while True:
	raw_sentence = raw_input("Input: ")
	#to get out of the loop type quit
	if raw_sentence == "quit":
		break
	#tokenise the sentence
	words = raw_sentence.split(" ")
	wordcount = 0
	ev = 0
	#iterate through words
	for word in words:
		#if word in dictionary add sentiment to average
		if word in dict:
			wordcount += 1
			ev += dict[word]
		else:
			print word +" not in dictionary"
	#print average if averagable, if not print error
	if wordcount == 0:
		print "No word in dictionary."
	else:
		ev = ev/float(wordcount)
		print "Evaluation: "+str(ev)