#!/usr/bin/env python
import json, featurebuilder as f

#SETTINGS:
sentences = json.loads(open("data/dev.txt.json").read())
dictionary = json.loads(open("data/dictionary.json").read())
feature_accuracy_sets = [4]
features = [f.ignore2,f.onlyjj,f.onlyknown,f.general]
sentiment_accuracy = 2

#CODE:
numericals = []
for f_func in features:
		for acc in feature_accuracy_sets:
			numericals += f_func("header",acc)	
numericals.sort()
output = ["%Automatically built ARFF-file"]
output += ["%Feature sets: "+str([x.__name__ for x in features])]
output += ["%Accuracies: "+str(feature_accuracy_sets)]
output += ["%Sentiment classes: "+str(sentiment_accuracy)]
output += ["@RELATION sentiment"]
output += [""]
output += ["@ATTRIBUTE "+n+" NUMERIC" for n in numericals]
output += ["@ATTRIBUTE sentiment {"+",".join([str(x) for x in range(sentiment_accuracy+1)])+"}"] 
output += [""]
output += ["@DATA"]
numericals += ["sentiment"]
data = []
for sentence_c in sentences:
	feature_row = {}
	feature_row["sentiment"] =  int(round(int(sentence_c[0])/4.0*sentiment_accuracy))
	sentence = sentence_c[1]
	for f_func in features:
		for acc in feature_accuracy_sets:
			ftc = f_func(sentence,acc,dictionary)
			feature_row = dict(feature_row.items() + ftc.items())
	output += [",".join([str(feature_row[n]) for n in numericals])]
print "\n".join(output)