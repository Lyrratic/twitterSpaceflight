import json
import io
import csv
from numpy import genfromtxt

ESA = ["astro_Jfrancois", "astro_timpeake", "Thom_astro", "Astro_Alex", "AstroSamantha", "astro_luca", "astro_andre", "astro_paolo", "Astro_Andreas", "CFuglesang", "ESA_EAC", "esa", "esaoperations"]
JAXA = ["Astro_Satoshi", "Astro_Wakata", "Astro_Soichi", "Astro_Kimiya", "JAXA_en", "Aki_Hoshide"]
CSA = ["csa_asc", "asc_csa", "Astro_Jeremy", "Astro_DavidS", "AstroDaveMD", "Cmdr_Hadfield", "RobertaBondar", "RobertThirsk", "AstroGarneau"]
Roscosmos = ["fka_roscosmos", "spacetihon", "OlegMKS", "Msuraev", "AntonAstrey"]
NASA = ["NASA","NASA_Astronauts","NASAPeople","AstroClass2013","SciAstro","Astro_Flow","Astro_Cady","Astro_Ferg","AstroCoastie","astro_Pettit","AstroDot","Astro_Wheels","Astro_Doug","Astro_Taz","Astro_Box","Astro2fish","Astro_Jeff","AstroAcaba","AstroKarenN","Astro_Kate7","astro_kjell","Astro_127","AstroIronMike","foreman_mike","astro_aggie","AstroIllini","Astro_Mike","Astro_Nicholas","Astro_Nicole","astro_reid","Astro_Rex","AstroRM","Astro_Ron","Astro_Sandy","AstroSerena","StationCDRKelly","Astro_Maker","Astro_Suni","AstroTerry","astro_tim","AstroMarshburn","Astro_TJ","Chief_Astronaut","Commercial_Crew","DESERT_RATS","HMP","ISS_Research","NASAMightyEagle","NASA_NEEMO","NASA_Orion","PavilionLake","MorpheusLander","AstroRobonaut","NASA_SLS","Astro_Clay"]

groups = ["ESA", "JAXA", "CSA", "Roscosmos", "NASA"]

def getGroup(groupName):
    if groupName == "ESA":
        return ESA 
    if groupName == "JAXA": 
        return  JAXA 
    if groupName == "CSA": 
        return  CSA 
    if groupName == "Roscosmos": 
        return  Roscosmos 
    if groupName == "NASA": 
        return  NASA 

allNames = ESA+JAXA+CSA+Roscosmos+NASA
allTweetNums = []

# open file and create reader
for gName in groups:
    group = getGroup(gName)
    for member in group:
        with open('../1215-415_data/'+member+'_tweets.csv', 'rb') as f:
            counter = 0
            reader = csv.reader(f, delimiter=',', quotechar='"', skipinitialspace=True)
            # read header
            header = reader.next()
            # read rows, append values to lists
            for row in reader:
                counter +=1

            allTweetNums.append(counter)
print len(allTweetNums)
print len(allNames)
print allTweetNums