#!/usr/bin/env python
import json, featurebuilder as f
feature_accuracy_sets = [4]
features = [f.onlyknown]
sentiment_accuracy = 4
dictionary = json.loads(open("data/dictionary.json").read())
sentences = [["3", [["It", "PRP"], ["'s", "VBZ"], ["a", "DT"], ["lovely", "JJ"], ["film", "NN"], ["with", "IN"], ["lovely", "JJ"], ["performances", "NNS"], ["by", "IN"], ["Buy", "JJ"], ["and", "CC"], ["Accorsi", "NNP"], [".", "."]]]]
output = []
for sentence_c in sentences:
	feature_row = {}
	feature_row["sentiment"] =  round(int(sentence_c[0])/4.0*sentiment_accuracy)
	sentence = sentence_c[1]
	for f_func in features:
		for acc in feature_accuracy_sets:
			ftc = f_func(sentence,acc,dictionary)
			feature_row = dict(feature_row.items() + ftc.items())
	output.append(feature_row)
print output