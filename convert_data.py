#!/usr/bin/env python

#University of Heidelberg
#Institute of Computational Linguistics
#Designing Experiments for Machine Learning Tasks
#Project Sentiment Analysis 2
#Dominik Both, Denis Orechov
#2014-2015

#This script converts the test and training data of the Stanford Sentiment Bank in to a JSON Format and annotates it with POS-Tags using the Stanford POS Tagger
#How to use: converter.py file_to_convert.txt

import sys, json, os, time
from nltk.tag.stanford import POSTagger
try:
	#Get the filename from the terminal-arguments and create output name by appending the json file ending
	filename = sys.argv[1]
	outputname = filename+".json"
	#load the pos-tagger
	st = POSTagger(os.path.dirname(os.path.realpath(__file__))+'/ext/postagger/models/english-bidirectional-distsim.tagger',os.path.dirname(os.path.realpath(__file__))+'/ext/postagger/stanford-postagger.jar','utf-8') 
	out = []
	#replace array to get rid of the tree structure... A mistake in retrospect.
	replace = ["(1 ","(2 ","(3 ","(4 ","(0 ",")"]
	#number of sentences for estimated finishing calculation
	num_lines = sum(1 for line in open(filename))
	with open(filename) as fileobject:
		#linecounter
		xy = 1
		temp = "No previous calculation"
		#set begin time for estimated finishing calculation
		begintime = time.clock()
		for line in fileobject:
			#clear the commandline
			os.system('cls' if os.name == 'nt' else 'clear')
			print "expml converter v1.0 - d.both, d.orechov - icl heidelberg"
			#percentage
			print "Calculating: "+str(round(float(xy)/num_lines*100,1))+"%"
			#calculate elapsed time
			now = time.clock()
			vg = now-begintime
			#somehow on unix time.clock() is in another unit as it is on msdos. if used on dos this line as to be ommitted.
			vg *= 60
			#simple rule of proportion, time since start divided by percentage is time that is needed for 100%
			seconds = vg/(float(xy)/num_lines*100)*100
			#subtract elapsed time to get remaining time
			seconds -= vg
			#calculate minutes and hours out of seconds
			m, s = divmod(seconds, 60)
			h, m = divmod(m, 60)
			#print remaining 
			print "Remaining: %02d:%02d:%02d hours" % (h, m, s)
			print
			#so we humans have something to watch, show the last calculated sentence
			print "Last calculation: "+str(temp)
			#sentiment class of the whole sentence is always the second character of the sentence in this lisp-like structure
			sclass = line[1]
			#get rid of tree structure..
			for x in replace:
				line = line.replace(x,"").strip()
			#pos-tag the sentence and append it to the output list
			temp = [sclass,st.tag(line.split(" "))]
			out.append(temp)
			#increment line counter
			xy += 1
	#write output list into json file
	f = open(outputname,"w")
	f.write(json.dumps(out))
	f.close()		
except:
	print "No file specified or file not found."