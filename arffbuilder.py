#!/usr/bin/env python

#University of Heidelberg
#Institute of Computational Linguistics
#Designing Experiments for Machine Learning Tasks
#Project Sentiment Analysis 2
#Dominik Both, Denis Orechov
#2014-2015

#Builds arff-files for further use in WEKA.

#How to use: Settings below. Redirect output in arff-file using greater-than sign.

import json, featurebuilder as f

#SETTINGS:
sentences = json.loads(open("data/train.txt.json").read())
dictionary = json.loads(open("data/dictionary.json").read())
#choose feature functions (given in featurebuilder.py) to include in arff-file
features = [f.max_sentiment,f.min_sentiment]

#CODE:
#inititialise list of features
numericals = []
#fill feature list by getting the headers of chosen featurebuilders
for f_func in features:
	numericals += f_func("header")
#sort the features for better readability
numericals.sort()
#add sentiment class to header
numericals += [["sentiment","{0,1,2,3,4}"]]
#build header
output = ["%Automatically built ARFF-file"]
#write used configuration in header
output += ["%Feature sets: "+str([x.__name__ for x in features])]
#write features in header
output += ["@RELATION sentiment"]
output += [""]
output += ["@ATTRIBUTE "+n[0]+" "+n[1] for n in numericals]
output += [""]
output += ["@DATA"]
data = []
#calculate data
#iterate through sentences
for sentence_c in sentences:
	feature_row = {}
	#set target sentiment
	feature_row["sentiment"], sentence =  sentence_c
	#get all features by sending the sentence to all chosen featurebuilders. add returned features to storage
	for f_func in features:
		ftc = f_func(sentence,dictionary)
		feature_row = dict(feature_row.items() + ftc.items())
	#retrieve features in the same order that they are in the header
	output += [",".join([str(feature_row[n[0]]) for n in numericals])]
#flush buffer
print "\n".join(output)