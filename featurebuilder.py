def general(sentence = "header", accuracy = 4, dictionary = {}): #USES ALL WORDS
	feature_prefix = "all"
	if sentence == "header":
		#output header @ATTRIBUTE line
		return True
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
		return {feature_prefix+"-"+str(accuracy)+"-"+str(room): parts[room]/float(num_ct_words) for room in range(len(parts))}
		
def onlyknown(sentence = "header", accuracy = 4, dictionary = {}): #USES ALL WORDS
	feature_prefix = "known"
	if sentence == "header":
		#output header @ATTRIBUTE line
		return True
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
		return {feature_prefix+"-"+str(accuracy)+"-"+str(room): parts[room]/float(num_ct_words) for room in range(len(parts))}
				
def onlyjj(sentence = "header", accuracy = 4, dictionary = {}): #ONLY JJ (Adjectives)
	feature_prefix = "jj"
	if sentence == "header":
		#
		return True
	else:
		parts = [1 for x in range(accuracy+1)]
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
		return {feature_prefix+"-"+str(accuracy)+"-"+str(room): parts[room]/float(num_ct_words) for room in range(len(parts))}