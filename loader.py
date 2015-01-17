import re, json
l = {}
l2 = {}
r = {}
with open("ext/sentimentbank/dictionary.txt") as fileobject:
    for line in fileobject:
		lines = line.split("|")
		if re.match("^[A-Za-z']*$", lines[0]):
			l[lines[1].strip()] = lines[0]
with open("ext/sentimentbank/sentiment_labels.txt") as fileobject:
    for line in fileobject:
		lines = line.split("|")
		try:
			raw_st = float(lines[1].strip())
			sentiment = raw_st * 4
			l2[lines[0].strip()] = sentiment
		except:
			print "Line ignored"
for key in l:
	r[l[key]] = l2[key]
f = open("data/dictionary.json","w")
f.write(json.dumps(r))
f.close()
print "Done. Dictionary contains "+str(len(r))+" items."