#!/usr/bin/env python

#University of Heidelberg
#Institute of Computational Linguistics
#Designing Experiments for Machine Learning Tasks
#Project Sentiment Analysis 2
#Dominik Both, Denis Orechov
#2014-2015

#Well big mistake happened when we assumed the annotation of the sentence in the training data as target, when it was calculated. Meanwhile the real human annotated data slumbered in the dictionary.. This script fixes this and updates the target sentiment in the training test etc file to the real value.

#How to use: updater.py file.json

import json, timeit, sys
start = timeit.default_timer()

to_update = json.loads(open(sys.argv[1]).read())
dictionary = json.loads(open("data/dictionary.json").read())
newname = sys.argv[1]+"_u.json"
new = []
for sentence_line in to_update:
	word_list = sentence_line[1]
	sentence = " ".join([x[0] for x in word_list])
	if (sentence in dictionary):
		sentence_line[0] = dictionary[sentence]
	else:
		print sentence+" was not found"
	new.append(sentence_line)
f = open(newname,"w")
f.write(json.dumps(new))
f.close()
stop = timeit.default_timer()
print "Done. Calculated in "+str(stop - start) +" seconds."

