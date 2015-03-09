import csv

ESA = ["astro_Jfrancois", "astro_timpeake", "Thom_astro", "Astro_Alex", "AstroSamantha", "astro_luca", "astro_andre", "astro_paolo", "Astro_Andreas", "CFuglesang", "ESA_EAC", "esa", "esaoperations"]
JAXA = ["Astro_Satoshi", "Astro_Wakata", "Astro_Soichi", "Astro_Kimiya", "JAXA_en", "Aki_Hoshide"]
CSA = ["csa_asc", "asc_csa", "Astro_Jeremy", "Astro_DavidS", "AstroDaveMD", "Cmdr_Hadfield", "RobertaBondar", "RobertThirsk", "AstroGarneau"]
Roscosmos = ["fka_roscosmos", "spacetihon", "OlegMKS", "Msuraev", "AntonAstrey"]
NASA = [
"NASA",
"NASA_Astronauts",
"NASAPeople",
"AstroClass2013",
"SciAstro",
"Astro_Flow",
"Astro_Cady",
"Astro_Ferg",
"Astro_Clay",
"AstroCoastie",
"astro_Pettit",
"AstroDot",
"Astro_Wheels",
"Astro_Doug",
"Astro_Taz",
"Astro_Box",
"Astro2fish",
"Astro_Jeff",
"AstroAcaba",
"AstroKarenN",
"Astro_Kate7",
"astro_kjell",
"Astro_127",
"AstroIronMike",
"foreman_mike",
"astro_aggie",
"AstroIllini",
"Astro_Mike",
"Astro_Nicholas",
"Astro_Nicole",
"astro_reid",
"Astro_Rex",
"AstroRM",
"Astro_Ron",
"Astro_Sandy",
"AstroSerena",
"StationCDRKelly",
"Astro_Maker",
"Astro_Suni",
"AstroTerry",
"astro_tim",
"AstroMarshburn",
"Astro_TJ",
"Chief_Astronaut",
"Commercial_Crew",
"DESERT_RATS",
"HMP",
"ISS_Research",
"NASAMightyEagle",
"NASA_NEEMO",
"NASA_Orion",
"PavilionLake",
"MorpheusLander",
"AstroRobonaut",
"NASA_SLS"
]

groups = ["ESA", "JAXA", "CSA", "Roscosmos", "NASA"]

def getGroup(group_name):
    if group_name == "ESA": return ESA 
    if group_name == "JAXA": return JAXA 
    if group_name == "CSA": return CSA 
    if group_name == "Roscosmos": return Roscosmos 
    if group_name == "NASA": return NASA 

fout = csv.writer(open("filterCountReplies.csv", "wb"))
fout.writerow(["has","prefers","count"])

for g in groups:
	#fout=open(g+"_filterCountReplies.csv","a")
	esaCount = 0
	jaxaCount = 0
	csaCount = 0
	rosCount = 0
	nasaCount = 0
	# loop through group members:
	group = getGroup(g)
	print "now printing: " + g
	for line in open("../2014data/orgs/" + g + "_replies.csv"):
	    #print "line: " + line
	    fixLine = line.replace("\n", "");
	    if fixLine in ESA:
	    	esaCount += 1
	    elif fixLine in JAXA:
	    	jaxaCount += 1
	    elif fixLine in CSA:
	    	csaCount += 1
	    elif fixLine in Roscosmos:
	    	rosCount += 1
	    elif fixLine in NASA:
	    	nasaCount += 1
	print "ESA/JAXA/CSA/Roscosmos/NASA: " + str(esaCount), str(jaxaCount), str(csaCount), str(rosCount), str(nasaCount)
	#fout.write(line)
	fout.writerow([g,"ESA",esaCount])
	fout.writerow([g,"JAXA",jaxaCount])
	fout.writerow([g,"CSA",csaCount])
	fout.writerow([g,"Roscosmos",rosCount])
	fout.writerow([g,"NASA",nasaCount])
#fout.close()