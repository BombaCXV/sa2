#!/usr/bin/env python

#University of Heidelberg
#Institute of Computational Linguistics
#Designing Experiments for Machine Learning Tasks
#Project Sentiment Analysis 2
#Dominik Both, Denis Orechov
#2014-2015

#Function container for feature functions.

#Format of a feature building function:
#Takes:
#sentence: Tokenised Sentence as list of words OR string "header"
#dictionary: Sentiment Dictionary format lemma->sentiment
#Returns:
#if header: List of features this function creates as a list pair of feature name and feature type.
#else: Dictionary feature_name->feature_value

#max_sentiment: maximum sentiment of all known words in sentence
def max_sentiment(sentence = "header", dictionary = {}):
	feature_prefix = "max_sentiment"
	if sentence == "header": return [[feature_prefix,"NUMERIC"]]
	max_sentiment = -1
	for word_c in sentence:
		word, pos = word_c
		if (word in dictionary and dictionary[word] > max_sentiment):
			max_sentiment = dictionary[word]
	return {feature_prefix: max_sentiment}
	
#min_sentiment: minimum sentiment of all known words in sentence
def min_sentiment(sentence = "header", dictionary = {}):
	feature_prefix = "min_sentiment"
	if sentence == "header": return [[feature_prefix,"NUMERIC"]]
	min_sentiment = 5
	for word_c in sentence:
		word, pos = word_c
		if (word in dictionary and dictionary[word] < min_sentiment):
			min_sentiment = dictionary[word]
	return {feature_prefix: min_sentiment}