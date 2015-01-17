import json
try:
	json_data2 = open("data/dictionary.json").read()
	dict = json.loads(json_data2)
	while True:
		raw_sentence = raw_input("Input: ")
		if raw_sentence == "quit":
			break
		words = raw_sentence.split(" ")
		wordcount = 0
		ev = {}
		
		for word in words:
			if word in dict:
				
				wordcount += 1
				ev[dict[word]
				print fkt
				print dict[word]
			else:
				print word +" not in dictionary"
		if wordcount == 0:
			print "No word in dictionary."
		else:
			
			
			print "Evaluation: "+ev
except:
	print "Somewhere, sometime there was an error."