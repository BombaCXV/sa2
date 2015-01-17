import sys, json
try:
	filename = sys.argv[1]
	json_data=open(filename).read()
	ev_data = json.loads(json_data)
	json_data2 = open("data/dictionary.json").read()
	dict = json.loads(json_data2)
	eval = 0
	right = 0
	for sentence in ev_data:
		soll = float(sentence[0])
		words = sentence[1]
		wordcount = 0
		evsum = 0
		
		for word_l in words:
			word = word_l[0]
			if word in dict:
				if round(dict[word]) != 2:
					wordcount += 1
					evsum += dict[word]
		if wordcount == 0:
			print "No word in dictionary."
		else:
			
			ev = evsum/(1.0*wordcount)
			eval += 1
			
			
			if ev < 2:
				eva = "-"
		
			
			if ev >= 2:
				eva = "+"
			if soll < 2:
				evasoll = "-"
			
			if soll >= 2:
				evasoll = "+"
			print "Ev: "+eva+" Is: "+evasoll
			if evasoll == eva:
				right += 1
	print "Accuracy: "+str(1.0*right/eval*100)
	print "WOW!"
except:
	print "No file specified or file not found."