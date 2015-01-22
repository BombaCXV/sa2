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
	negation_words = ["not","n't","less","least","no"]
	negation = False
	ignore = []
	for index in range(len(sentence)):
		if index in ignore:
			continue
		possible_n_grams = len(sentence) - index
		if possible_n_grams >= len(sentence):
			possible_n_grams = len(sentence)-1 
		for end in range(index+1,possible_n_grams+index+1):
			searcher = " ".join([x[0] for x in sentence[index:end]])
			if searcher in dictionary:
				ignore += range(index,end)
				reals = searcher
		if negation:
			if dictionary[reals] < 0.5:
				new_r = dictionary[reals] + 0.4
				negation = False
			else:
				new_r = dictionary[reals] - 0.4
				negation = False
		else:
			new_r = dictionary[reals]
		if (new_r > max_sentiment):
			max_sentiment = new_r
			if reals in negation_words:
				negation = True
	if (max_sentiment != 0.5 or True):
		return {feature_prefix: max_sentiment}
	else:
		return {feature_prefix: "?"}
	
def avg_sentiment_no_neutral(sentence = "header", dictionary = {}):
	feature_prefix = "avg_sentiment_no_neutral"
	if sentence == "header": return [[feature_prefix,"NUMERIC"]]
	cnt = 0
	avg = 0
	ignore = []
	negation_words = ["not","n't","less","least","no"]
	negation = False
	bf = "NEW\n";
	for index in range(len(sentence)):
		reals = "SICHER NICHT IM DICTIONARY"
		if index in ignore:
			continue
		possible_n_grams = len(sentence) - index
		if possible_n_grams >= 8:
			possible_n_grams = 8 
		for end in range(index+1,possible_n_grams+index+1):
			searcher = " ".join([x[0] for x in sentence[index:end]])
			if searcher in dictionary:
				ignore += range(index,end)
				reals = searcher
		bf += reals+str(dictionary[reals])+"\n"
		if (dictionary[reals] < 0.4 or dictionary[reals] >= 0.6):
			if negation:
				if dictionary[reals] < 0.5:
					new_r = dictionary[reals] + 0.4
				else:
					new_r = dictionary[reals] - 0.4
				avg += new_r*len(reals.split())
				negation = False
			else:
				avg += dictionary[reals]*len(reals.split())
				negation = False
			cnt += len(reals.split())
			if reals in negation_words:
				negation = True
		
	if (cnt == 0):
		return {feature_prefix: "?"}
	else:
		return {feature_prefix: avg/cnt}	
	
#min_sentiment: minimum sentiment of all known words in sentence
def min_sentiment(sentence = "header", dictionary = {}):
	feature_prefix = "min_sentiment"
	if sentence == "header": return [[feature_prefix,"NUMERIC"]]
	min_sentiment = 5
	ignore = []
	negation_words = ["not","n't","less","least","no"]
	negation = False
	for index in range(len(sentence)):
		if index in ignore:
			continue
		possible_n_grams = len(sentence) - index
		if possible_n_grams >= len(sentence):
			possible_n_grams = len(sentence)-1 
		for end in range(index+1,possible_n_grams+index+1):
			searcher = " ".join([x[0] for x in sentence[index:end]])
			if searcher in dictionary:
				ignore += range(index,end)
				reals = searcher
		if negation:
			if dictionary[reals] < 0.5:
				new_r = dictionary[reals] + 0.4
				negation = False
			else:
				new_r = dictionary[reals] - 0.4
				negation = False
		else:
			new_r = dictionary[reals]
		if (new_r < min_sentiment):
			min_sentiment = new_r
			if reals in negation_words:
				negation = True
	if (min_sentiment != 0.5 or True):
		return {feature_prefix: min_sentiment}
	else:
		return {feature_prefix: "?"}
		
		def avg_sentiment(sentence = "header", dictionary = {}):
	feature_prefix = "avg_sentiment"
	if sentence == "header": return [[feature_prefix,"NUMERIC"]]
	cnt = 0
	avg = 0
	ignore = []
	for index in range(len(sentence)):
		if index in ignore:
			continue
		possible_n_grams = len(sentence) - index
		if possible_n_grams >= len(sentence):
			possible_n_grams = len(sentence)-1 
		for end in range(index+1,possible_n_grams+index+1):
			searcher = " ".join([x[0] for x in sentence[index:end]])
			if searcher in dictionary:
				ignore += range(index,end)
				reals = searcher
		avg += dictionary[reals]*len(reals.split())
		cnt += len(reals.split())
	return {feature_prefix: avg/cnt}

def baseline(sentence = "header", dictionary = {}):
	feature_prefix = "baseline"
	if sentence == "header": return [[feature_prefix,"NUMERIC"]]
	cnt = 0
	avg = 0
	ignore = []
	for word_c in sentence:
		word, pos = word_c
		if (word in dictionary):
			cnt += 1
			avg += dictionary[word]
	return {feature_prefix: avg/cnt}
	
def avg_sentiment_no_neutral_unigrams(sentence = "header", dictionary = {}):
	feature_prefix = "avg_sentiment_no_neutral_unigrams"
	if sentence == "header": return [[feature_prefix,"NUMERIC"]]
	cnt = 0
	avg = 0
	ignore = []
	negation_words = ["not","n't","less","least","no"]
	negation = False
	for word_c in sentence:
		reals, pos = word_c
		if (reals not in dictionary):
			continue
		if (dictionary[reals] < 0.4 or dictionary[reals] >= 0.6):
			if negation:
				if dictionary[reals] < 0.5:
					new_r = dictionary[reals] + 0.4
				else:
					new_r = dictionary[reals] - 0.4
				avg += new_r*len(reals.split())
				negation = False
			else:
				avg += dictionary[reals]*len(reals.split())
				negation = False
			cnt += len(reals.split())
			if reals in negation_words:
				negation = True
	if (cnt == 0):
		return {feature_prefix: "?"}
	else:
		return {feature_prefix: avg/cnt}	
		