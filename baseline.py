#!/usr/bin/env python

#University of Heidelberg
#Institute of Computational Linguistics
#Designing Experiments for Machine Learning Tasks
#Project Sentiment Analysis 2
#Dominik Both, Denis Orechov
#2014-2015

#baseline tester. uses only unigrams. reads json testdatafiles (as created by this project's convert_data script), classifies them using the average of known words, and evaluates this classification using the annotation of the stanford sentiment bank. Binary classification in + and -.

#How to use: baseline.py file_to_evaluate.json

#init
import sys, json
try:
	filename = sys.argv[1]
	json_data=open(filename).read()
	ev_data = json.loads(json_data)
	json_data2 = open("data/dictionary.json").read()
	dict = json.loads(json_data2)
	eval = 0
	right = 0
	prr = {}
	#iterate through sentences
	for sentence in ev_data:
		#get class-annotation of sentence
		soll = float(sentence[0])
		words = sentence[1]
		wordcount = 0
		evsum = 0
		#iterate through every word in sentence
		for word_l in words:
			
			word, pos = word_l
			#if word is known in dictionary add to counter for average
			if word in dict:
				wordcount += 1
				evsum += dict[word]
		#if no word is in the dictionary we do not evaluate this sentence because probably something is wrong
		if wordcount == 0:
			print "No word in dictionary."
		else:
			#sentiment of the sentence is average
			ev = evsum/(1.0*wordcount)
			#dictionary is in 0-1, so 0.5 is parting value.
			if ev < 0.5:
				eva = "-"
			if ev >= 0.5:
				eva = "+"
			#target is in 0-1, so 0.5 is parting value.
			if soll < 0.5:
				evasoll = "-"
			if soll >= 0.5:
				evasoll = "+"
			#for recall and precision save the actual and target class in dictionary
			if (evasoll+eva not in prr):
				prr[evasoll+eva] = 0
			prr[evasoll+eva] += 1
			print "Ev: "+eva+" Is: "+evasoll
			#for the correctness 
			eval += 1
			if evasoll == eva:
				right += 1
	#print evaluation
	print "Precision for positive sentences: "+str(1.0*prr["++"]/(prr["++"]+prr["-+"])*100)
	print "Recall for positive sentences: "+str(1.0*prr["++"]/(prr["++"]+prr["+-"])*100)
	print "Precision for negative sentences: "+str(1.0*prr["--"]/(prr["--"]+prr["+-"])*100)
	print "Recall for negative senctences: "+str(1.0*prr["--"]/(prr["--"]+prr["-+"])*100)
	print "Correctness: "+str(1.0*right/eval*100)
except:
	print "No file specified or file not found."