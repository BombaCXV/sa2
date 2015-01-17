#!/usr/bin/env python
import sys, json, os, time
from nltk.tag.stanford import POSTagger
if True:
	filename = sys.argv[1]
	outputname = filename+".json"
	st = POSTagger(os.path.dirname(os.path.realpath(__file__))+'/ext/postagger/models/english-bidirectional-distsim.tagger',os.path.dirname(os.path.realpath(__file__))+'/ext/postagger/stanford-postagger.jar','utf-8') 
	out = []
	replace = ["(1 ","(2 ","(3 ","(4 ","(0 ",")"]
	num_lines = sum(1 for line in open(filename))
	with open(filename) as fileobject:
		xy = 1
		temp = "No previous calculation"
		begintime = time.clock()
		for line in fileobject:
			
			os.system('cls' if os.name == 'nt' else 'clear')
			print "expml converter v1.0 - d.both, d.orechov - icl heidelberg"
			print "Calculating: "+str(round(float(xy)/num_lines*100,1))+"%"
			now = time.clock()
			vg = now-begintime
			vg *= 60 #linux
			seconds = vg/(float(xy)/num_lines*100)*100
			#print seconds
			seconds -= vg
			#print seconds
			m, s = divmod(seconds, 60)
			h, m = divmod(m, 60)
			
			print "Remaining: %02d:%02d:%02d hours" % (h, m, s)
			print
			print "Last calculation: "+str(temp)
			sclass = line[1]
			for x in replace:
				line = line.replace(x,"").strip()
			temp = [sclass,st.tag(line.split(" "))]
			out.append(temp)
			xy += 1
	f = open(outputname,"w")
	f.write(json.dumps(out))
	f.close()		
#except:
#	print "No file specified or file not found."