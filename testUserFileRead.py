import json
import io

#reads twitter user json files

#all the users:
allAccounts = ["astro_Jfrancois", "astro_timpeake", "Thom_astro", 
"Astro_Alex", "AstroSamantha", "astro_luca", "astro_andre", 
"astro_paolo", "Astro_Andreas", "CFuglesang", "ESA_EAC", "esa", "esaoperations",
"Astro_Satoshi", "Astro_Wakata", "Astro_Soichi", "Astro_Kimiya", "JAXA_en", 
"Aki_Hoshide", "csa_asc", "asc_csa", "Astro_Jeremy", "Astro_DavidS", 
"AstroDaveMD", "Cmdr_Hadfield", "RobertaBondar", "RobertThirsk", "AstroGarneau",
"fka_roscosmos", "spacetihon", "OlegMKS", "Msuraev", "AntonAstrey",
"NASA","NASA_Astronauts","NASAPeople","AstroClass2013","SciAstro","Astro_Flow",
"Astro_Cady","Astro_Ferg","Astro_Clay","AstroCoastie","astro_Pettit","AstroDot",
"Astro_Wheels","Astro_Doug","Astro_Taz","Astro_Box","Astro2fish","Astro_Jeff",
"AstroAcaba","AstroKarenN","Astro_Kate7","astro_kjell","Astro_127","AstroIronMike",
"foreman_mike","astro_aggie","AstroIllini","Astro_Mike","Astro_Nicholas",
"Astro_Nicole","astro_reid","Astro_Rex","AstroRM","Astro_Ron","Astro_Sandy",
"AstroSerena","StationCDRKelly","Astro_Maker","Astro_Suni","AstroTerry",
"astro_tim","AstroMarshburn","Astro_TJ","Chief_Astronaut","Commercial_Crew",
"DESERT_RATS","HMP","ISS_Research","NASAMightyEagle","NASA_NEEMO","NASA_Orion",
"PavilionLake","MorpheusLander","AstroRobonaut","NASA_SLS"]

#separated by group:
ESA = ["astro_Jfrancois", "astro_timpeake", "Thom_astro", "Astro_Alex", 
"AstroSamantha", "astro_luca", "astro_andre", "astro_paolo", "Astro_Andreas", 
"CFuglesang", "ESA_EAC", "esa", "esaoperations"]
JAXA = ["Astro_Satoshi", "Astro_Wakata", "Astro_Soichi", "Astro_Kimiya", 
"JAXA_en", "Aki_Hoshide"]
CSA = ["csa_asc", "asc_csa", "Astro_Jeremy", "Astro_DavidS", "AstroDaveMD", 
"Cmdr_Hadfield", "RobertaBondar", "RobertThirsk", "AstroGarneau"]
Roscosmos = ["fka_roscosmos", "spacetihon", "OlegMKS", "Msuraev", "AntonAstrey"]
NASA = [
"NASA","NASA_Astronauts","NASAPeople","AstroClass2013","SciAstro","Astro_Flow",
"Astro_Cady","Astro_Ferg","Astro_Clay","AstroCoastie","astro_Pettit","AstroDot",
"Astro_Wheels","Astro_Doug","Astro_Taz","Astro_Box","Astro2fish","Astro_Jeff",
"AstroAcaba","AstroKarenN","Astro_Kate7","astro_kjell","Astro_127","AstroIronMike",
"foreman_mike","astro_aggie","AstroIllini","Astro_Mike","Astro_Nicholas",
"Astro_Nicole","astro_reid","Astro_Rex","AstroRM","Astro_Ron","Astro_Sandy",
"AstroSerena","StationCDRKelly","Astro_Maker","Astro_Suni","AstroTerry",
"astro_tim","AstroMarshburn","Astro_TJ","Chief_Astronaut","Commercial_Crew",
"DESERT_RATS","HMP","ISS_Research","NASAMightyEagle","NASA_NEEMO","NASA_Orion",
"PavilionLake","MorpheusLander","AstroRobonaut","NASA_SLS"]
 
groups = ["ESA", "JAXA", "CSA", "Roscosmos", "NASA"]

# fields = ["screen_name", "name", "id", "profile_image", "location", "description", "created_at", "followers_count", "following_count", "tweets_count", "favorites_count"]
fields = ["screen_name", "name", "id", "created_at", "followers_count", "following_count", "tweets_count", "favorites_count"]

#new file for the big csv
OUTPUT_FILE = 'NASA.csv'
# f = open(OUTPUT_FILE, 'w')
f = io.open(OUTPUT_FILE, 'w', encoding='utf8')

#get the headings
for field in fields:
	# f.write(field + ',')
	f.write(unicode(field) + ',')

# f.seek(0, os.SEEK_END) #cut off last comma
# f.truncate()
# f.write('\n')
f.write(unicode('\n'))


#go through each user
for name in NASA:
	print name
	json_data=open('data/JSONs/' + name + '.txt') #open file for that person

	data = json.load(json_data)
	for field in fields:
		# f.write(str(data[field]) + ',')
		f.write(unicode(data[field]) + ',')
	# f.seek(0, os.SEEK_END) #cut off last comma
	# f.truncate()
	# f.write('\n')
	f.write(unicode('\n'))
	json_data.close()
f.close()

