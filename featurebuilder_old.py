#DEPRECATED

def general(sentence = "header", accuracy = 4, dictionary = {}): #USES ALL WORDS
	feature_prefix = "all"
	if sentence == "header":
		#output header @ATTRIBUTE line
		return [feature_prefix+"-"+str(accuracy)+"-"+str(room) for room in range(accuracy+1)]
	else:
		#create dictionary of features for the given sentence
		#Dictionary values are floating point numbers from 0-4. Those values get divided with 4, so we get a scale from 0-1 which gets multiplied with the accuracy and then rounded to whole numbers.
		#Those whole numbers are building features, describing the percentage of this sentiment value under all words in the set. 		
		#Example: 
		#Senctence: ["3", [["Birthday", "NN"], ["Girl", "NNP"], ["is", "VBZ"], ["an", "DT"], ["amusing", "JJ"], ["joy", "NN"], ["ride", "NN"], [".", "."]]]
		#Accuracy: 4
		#Output: {"class": 3, "all-4-0": 0.453, "all-4-1": 0.454 ...}
		parts = [0 for x in range(accuracy+1)]
		num_ct_words = 0
		for word_c in sentence:
			word = word_c[0]
			pos = word_c[1]
			if (True): #here we can make distinctions between pos or else, so that not every word gets counted
				if word in dictionary: #if word is not in dictionary we assume 2 as sentiment. if those words should not appear get rid of them one line above
					sentiment_c = dictionary[word]/4.0
				else:
					sentiment_c = 0.5
				num_ct_words += 1
				sentiment = int(round(accuracy * sentiment_c))
				parts[sentiment] += 1
		if num_ct_words:
			return {feature_prefix+"-"+str(accuracy)+"-"+str(room): parts[room]/float(num_ct_words) for room in range(accuracy+1)}
		else:
			return {feature_prefix+"-"+str(accuracy)+"-"+str(room): "0" for room in range(accuracy+1)}
		
def onlyknown(sentence = "header", accuracy = 4, dictionary = {}): #USES ALL WORDS
	feature_prefix = "known"
	if sentence == "header":
		return [feature_prefix+"-"+str(accuracy)+"-"+str(room) for room in range(accuracy+1)]
	else:
		parts = [0 for x in range(accuracy+1)]
		num_ct_words = 0
		for word_c in sentence:
			word, pos = word_c
			if (word in dictionary): 
				if word in dictionary: 
					parts[int(round(accuracy * dictionary[word]/4.0))] += 1
				else:
					parts[int(round(accuracy * 0.5))] += 1
				num_ct_words += 1
		if num_ct_words:
			return {feature_prefix+"-"+str(accuracy)+"-"+str(room): parts[room]/float(num_ct_words) for room in range(accuracy+1)}
		else:
			return {feature_prefix+"-"+str(accuracy)+"-"+str(room): "0" for room in range(accuracy+1)}
			
def ignore2(sentence = "header", accuracy = 4, dictionary = {}): #USES ALL WORDS
	feature_prefix = "no2"
	if sentence == "header":
		return [feature_prefix+"-"+str(accuracy)+"-"+str(room) for room in range(accuracy+1)]
	else:
		parts = [0 for x in range(accuracy+1)]
		num_ct_words = 0
		for word_c in sentence:
			word, pos = word_c
			if (word in dictionary and int(round(dictionary[word])) != 2): 
				if word in dictionary: 
					parts[int(round(accuracy * dictionary[word]/4.0))] += 1
				else:
					parts[int(round(accuracy * 0.5))] += 1
				num_ct_words += 1
		if num_ct_words:
			return {feature_prefix+"-"+str(accuracy)+"-"+str(room): parts[room]/float(num_ct_words) for room in range(accuracy+1)}
		else:
			return {feature_prefix+"-"+str(accuracy)+"-"+str(room): "0" for room in range(accuracy+1)}

def has_negation(sentence = "header", accuracy = 4, dictionary = {}): #ONLY JJ (Adjectives)
	feature_prefix = "negation"
	if sentence == "header":
		return [feature_prefix]
	else:
		negation_words = ["not","no","least","never","none"]
		negation = False
		for word_c in sentence:
			word = word_c[0]
			pos = word_c[1]
			if (word in negation_words):
				negation = True
		if negation:
			return {feature_prefix: 1}
		else:
			return {feature_prefix: 0}
	

def mean_all_no_neutral_n(sentence = "header", accuracy = 4, dictionary = {}): #ONLY JJ (Adjectives)
	feature_prefix = "mannn"
	if sentence == "header":
		return [feature_prefix]
	else:
		dlist = []
		negation_words = ["not","no","least","never","none"]
		negation = False
		for word_c in sentence:
			word = word_c[0]
			pos = word_c[1]
			if (word in negation_words):
				negation = True
			if (word in dictionary):
				if (round(dictionary[word]) != 2):
					dlist.append(dictionary[word])
		
		if (len(dlist)):
			dcn = reduce(lambda x, y: x + y, dlist) / len(dlist)
			if (negation):
				dcn = dcn - (accuracy/2) * -1 + (accuracy/2)
			if (round(dcn) != 2):
				dcn = "?"
			return {feature_prefix: dcn}
		else:
			return {feature_prefix: "?"}	
			
def mean_jj_no_neutral_n(sentence = "header", accuracy = 4, dictionary = {}): #ONLY JJ (Adjectives)
	feature_prefix = "jjsn"	
	if sentence == "header":
		return [feature_prefix]
	else:
		dlist = []
		negation_words = ["not","no","least","never","none"]
		negation = False
		for word_c in sentence:
			word = word_c[0]
			pos = word_c[1]
			if (word in negation_words):
				negation = True
			if (word in dictionary and pos == "JJ"):
				if (round(dictionary[word]) != 2):
					dlist.append(dictionary[word])
		
		if (len(dlist)):
			dcn = reduce(lambda x, y: x + y, dlist) / len(dlist)
			if (negation):
				dcn = dcn - (accuracy/2) * -1 + (accuracy/2)
			if (round(dcn) != 2):
				dcn = "?"
			return {feature_prefix: dcn}
		else:
			return {feature_prefix: "?"}

def mean_nn_no_neutral_n(sentence = "header", accuracy = 4, dictionary = {}): #ONLY JJ (Adjectives)
	feature_prefix = "nnsn"
	if sentence == "header":
		return [feature_prefix]
	else:
		dlist = []
		negation_words = ["not","no","least","never","none"]
		negation = False
		for word_c in sentence:
			word = word_c[0]
			pos = word_c[1]
			if (word in negation_words):
				negation = True
			if (word in dictionary and pos == "NN"):
				if (round(dictionary[word]) != 2):
					dlist.append(dictionary[word])
		
		if (len(dlist)):
			dcn = reduce(lambda x, y: x + y, dlist) / len(dlist)
			if (negation):
				dcn = dcn - (accuracy/2) * -1 + (accuracy/2)
			if (round(dcn) != 2):
				dcn = "?"
			return {feature_prefix: dcn}
		else:
			return {feature_prefix: "?"}


def mean_all(sentence = "header", accuracy = 4, dictionary = {}): #ONLY JJ (Adjectives)
	feature_prefix = "ma"
	if sentence == "header":
		return [feature_prefix]
	else:
		dlist = []
		for word_c in sentence:
			word = word_c[0]
			pos = word_c[1]
			if (word in dictionary):
				dlist.append(dictionary[word])
		if (len(dlist)):
			return {feature_prefix: reduce(lambda x, y: x + y, dlist) / len(dlist)}
		else:
			return {feature_prefix: "2"}	
			
def mean_jj(sentence = "header", accuracy = 4, dictionary = {}): #ONLY JJ (Adjectives)
	feature_prefix = "jja"	
	if sentence == "header":
		return [feature_prefix]
	else:
		dlist = []
		for word_c in sentence:
			word = word_c[0]
			pos = word_c[1]
			if (word in dictionary and pos == "JJ"):
				dlist.append(dictionary[word])
		if (len(dlist)):
			return {feature_prefix: reduce(lambda x, y: x + y, dlist) / len(dlist)}
		else:
			return {feature_prefix: "2"}

def mean_nn(sentence = "header", accuracy = 4, dictionary = {}): #ONLY JJ (Adjectives)
	feature_prefix = "nna"
	if sentence == "header":
		return [feature_prefix]
	else:
		dlist = []
		for word_c in sentence:
			word = word_c[0]
			pos = word_c[1]
			if (word in dictionary and pos == "NN"):
				dlist.append(dictionary[word])
		if (len(dlist)):
			return {feature_prefix: reduce(lambda x, y: x + y, dlist) / len(dlist)}
		else:
			return {feature_prefix: "2"}	



	
def mean_all_no_neutral(sentence = "header", accuracy = 4, dictionary = {}): #ONLY JJ (Adjectives)
	feature_prefix = "mann"
	if sentence == "header":
		return [feature_prefix]
	else:
		dlist = []
		for word_c in sentence:
			word = word_c[0]
			pos = word_c[1]
			if (word in dictionary):
				if (round(dictionary[word]) != 2):
					dlist.append(dictionary[word])
		if (len(dlist) and round(reduce(lambda x, y: x + y, dlist) / len(dlist)) != 2):
			return {feature_prefix: reduce(lambda x, y: x + y, dlist) / len(dlist)}
		else:
			return {feature_prefix: "?"}	
			
def mean_jj_no_neutral(sentence = "header", accuracy = 4, dictionary = {}): #ONLY JJ (Adjectives)
	feature_prefix = "jjs"	
	if sentence == "header":
		return [feature_prefix]
	else:
		dlist = []
		for word_c in sentence:
			word = word_c[0]
			pos = word_c[1]
			if (word in dictionary and pos == "JJ"):
				if (round(dictionary[word]) != 2):
					dlist.append(dictionary[word])
		if (len(dlist) and round(reduce(lambda x, y: x + y, dlist) / len(dlist)) != 2):
			return {feature_prefix: reduce(lambda x, y: x + y, dlist) / len(dlist)}
		else:
			return {feature_prefix: "?"}

def mean_nn_no_neutral(sentence = "header", accuracy = 4, dictionary = {}): #ONLY JJ (Adjectives)
	feature_prefix = "nns"
	if sentence == "header":
		return [feature_prefix]
	else:
		dlist = []
		for word_c in sentence:
			word = word_c[0]
			pos = word_c[1]
			if (word in dictionary and pos == "NN"):
				if (round(dictionary[word]) != 2):
					dlist.append(dictionary[word])
		if (len(dlist) and round(reduce(lambda x, y: x + y, dlist) / len(dlist)) != 2):
			return {feature_prefix: reduce(lambda x, y: x + y, dlist) / len(dlist)}
		else:
			return {feature_prefix: "?"}			
			
def onlyjj(sentence = "header", accuracy = 4, dictionary = {}): #ONLY JJ (Adjectives)
	feature_prefix = "jj"
	if sentence == "header":
		return [feature_prefix+"-"+str(accuracy)+"-"+str(room) for room in range(accuracy+1)]
	else:
		parts = [0 for x in range(accuracy+1)]
		num_ct_words = 0
		for word_c in sentence:
			word = word_c[0]
			pos = word_c[1]
			if (pos == "JJ"): 
				if word in dictionary: 
					parts[int(round(accuracy * dictionary[word]/4.0))] += 1
				else:
					parts[int(round(accuracy * 0.5))] += 1
				num_ct_words += 1
		if num_ct_words:
			return {feature_prefix+"-"+str(accuracy)+"-"+str(room): parts[room]/float(num_ct_words) for room in range(accuracy+1)}
		else:
			return {feature_prefix+"-"+str(accuracy)+"-"+str(room): "0" for room in range(accuracy+1)}