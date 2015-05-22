import io
import tweepy
import csv
import json
import re
from datetime import datetime
from twitter import *

ESA =[847170962, 437520768, 390287262, 337886919, 290876018, 266464616, 173116059, 40426996, 62584402, 1088665734, 21436960, 17384099, 552582271]
JAXA = [207878118, 1081962504, 85891683, 569247858, 104989762, 390455433]
CSA = [93714983, 93714345, 351640699, 351621695, 40683302, 186154646, 1852479216, 833510688, 977412476]
Roscosmos = [2306083502, 842286996, 2459541229, 391494900, 2325202999]
NASA = [11348282, 43166813, 374517706, 1506369180, 484991854, 86336234, 91409081, 274151347, 277020058, 310804819, 557994355, 127958577, 275710913, 180419242, 179644633, 386915587, 62829259, 336179304, 1299995892, 1109421360, 35877766, 38222521, 183672041, 497139188, 225411266, 543582293, 28123862, 105263800, 52768208, 330921167, 284616690, 541158674, 82453323, 53175445, 602813224, 65647594, 537588875, 537555179, 1115148079, 41441873, 394246259, 87520051, 2543629379, 376819015, 15117459, 13873072, 189253902, 334811174, 135275592, 33602654, 14422617, 244208830, 161760542, 467739426, 109571377]

groups = ["ESA", "JAXA", "CSA", "Roscosmos", "NASA"]

def getGroup(group_name):
    if group_name == "ESA": return ESA 
    if group_name == "JAXA": return JAXA 
    if group_name == "CSA": return CSA 
    if group_name == "Roscosmos": return Roscosmos 
    if group_name == "NASA": return NASA 

#DO THE THIINNGGG
fout = csv.writer(open("followerMatrix.csv", "wb"))
fout.writerow(["has","prefers","count"])

for g in groups:
	esaCount = 0
	jaxaCount = 0
	csaCount = 0
	rosCount = 0
	nasaCount = 0
	allUsers = []
	# loop through group members:
	group = getGroup(g)
	# the file below is missing because it's too large for github
	allUsers.extend(line.strip() for line in open("../groupData/"+g+'_allfollowers.csv'))

	print len(allUsers)

	for u in allUsers:
	    if int(u) in ESA:
	    	esaCount += 1
	    elif int(u) in JAXA:
	    	jaxaCount += 1
	    elif int(u) in CSA:
	    	csaCount += 1
	    elif int(u) in Roscosmos:
	    	rosCount += 1
	    elif int(u) in NASA:
	    	nasaCount += 1
	print "ESA/JAXA/CSA/Roscosmos/NASA: " + str(esaCount), str(jaxaCount), str(csaCount), str(rosCount), str(nasaCount)
		
	fout.writerow(["ESA",g,esaCount])
	fout.writerow(["JAXA",g,jaxaCount])
	fout.writerow(["CSA",g,csaCount])
	fout.writerow(["Roscosmos",g,rosCount])
	fout.writerow(["NASA",g,nasaCount])