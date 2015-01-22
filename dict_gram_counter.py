#!/usr/bin/env python

#University of Heidelberg
#Institute of Computational Linguistics
#Designing Experiments for Machine Learning Tasks
#Project Sentiment Analysis 2
#Dominik Both, Denis Orechov
#2014-2015

#Counts max n-gram in dict

import json

dictionary = json.loads(open("data/dictionary.json").read())
n = 0
for lemma in dictionary:
	t_n = len(lemma.split())
	if (t_n > n):
		n = t_n
print "Max n: "+str(n)
	