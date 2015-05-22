import io
import csv
import json
import re
ESA =[847170962, 437520768, 390287262, 337886919, 290876018, 266464616, 173116059, 40426996, 62584402, 1088665734, 21436960, 17384099, 552582271]
JAXA = [207878118, 1081962504, 85891683, 569247858, 104989762, 390455433]
CSA = [93714983, 93714345, 351640699, 351621695, 40683302, 186154646, 1852479216, 833510688, 977412476]
Roscosmos = [2306083502, 842286996, 2459541229, 391494900, 2325202999]
NASA = [11348282, 43166813, 374517706, 1506369180, 484991854, 86336234, 91409081, 274151347, 277020058, 310804819, 557994355, 127958577, 275710913, 180419242, 179644633, 386915587, 62829259, 336179304, 1299995892, 1109421360, 35877766, 38222521, 183672041, 497139188, 225411266, 543582293, 28123862, 105263800, 52768208, 330921167, 284616690, 541158674, 82453323, 53175445, 602813224, 65647594, 537588875, 537555179, 1115148079, 41441873, 394246259, 87520051, 2543629379, 376819015, 15117459, 13873072, 189253902, 334811174, 135275592, 33602654, 14422617, 244208830, 161760542, 467739426, 109571377]

ESA_names = ["astro_Jfrancois", "astro_timpeake", "Thom_astro", "Astro_Alex", "AstroSamantha", "astro_luca", "astro_andre", "astro_paolo", "Astro_Andreas", "CFuglesang", "ESA_EAC", "esa", "esaoperations"]
JAXA_names = ["Astro_Satoshi", "Astro_Wakata", "Astro_Soichi", "Astro_Kimiya", "JAXA_en", "Aki_Hoshide"]
CSA_names = ["csa_asc", "asc_csa", "Astro_Jeremy", "Astro_DavidS", "AstroDaveMD", "Cmdr_Hadfield", "RobertaBondar", "RobertThirsk", "AstroGarneau"]
Roscosmos_names = ["fka_roscosmos", "spacetihon", "OlegMKS", "Msuraev", "AntonAstrey"]
NASA_names = ["NASA","NASA_Astronauts","NASAPeople","AstroClass2013","SciAstro","Astro_Flow","Astro_Cady","Astro_Ferg","AstroCoastie","astro_Pettit","AstroDot","Astro_Wheels","Astro_Doug","Astro_Taz","Astro_Box","Astro2fish","Astro_Jeff","AstroAcaba","AstroKarenN","Astro_Kate7","astro_kjell","Astro_127","AstroIronMike","foreman_mike","astro_aggie","AstroIllini","Astro_Mike","Astro_Nicholas","Astro_Nicole","astro_reid","Astro_Rex","AstroRM","Astro_Ron","Astro_Sandy","AstroSerena","StationCDRKelly","Astro_Maker","Astro_Suni","AstroTerry","astro_tim","AstroMarshburn","Astro_TJ","Chief_Astronaut","Commercial_Crew","DESERT_RATS","HMP","ISS_Research","NASAMightyEagle","NASA_NEEMO","NASA_Orion","PavilionLake","MorpheusLander","AstroRobonaut","NASA_SLS","Astro_Clay"]

everyone = ESA_names+JAXA_names+CSA_names+Roscosmos_names+NASA_names
everyoneID = ESA + JAXA + CSA + Roscosmos + NASA
groups = ["ESA", "JAXA", "CSA", "Roscosmos", "NASA"]
groups_names = ["ESA_names", "JAXA_names", "CSA_names", "Roscosmos_names", "NASA_names"]

def getGroup(group_name):
    if group_name == "ESA": return ESA 
    if group_name == "JAXA": return JAXA 
    if group_name == "CSA": return CSA 
    if group_name == "Roscosmos": return Roscosmos 
    if group_name == "NASA": return NASA 

def getFromName(mem):
    if mem in ESA_names: return 1
    if mem in JAXA_names: return 2
    if mem in CSA_names: return 3
    if mem in Roscosmos_names: return 4
    if mem in NASA_names: return 5

#Create the array of nodes:
nodeArr = []
tempNodes = []
#loop through all the group member's files and count replies+retweets,
#create links array
linksArr = []
groupIndex= 1
nodeIndex = 0
gotLinks = []

#read in the follower csv info
with open('followerLinks.csv', 'rb') as f:
    reader = csv.reader(f)
    gotLinks = list(reader)
# print gotLinks

for oneLink in gotLinks:
    source = oneLink[0]
    target = oneLink[1]
    follows = oneLink[2]
    followedBy = oneLink[3]
    value = 0
    if follows == "True":
        value += 1
    if followedBy == "True":
        value += 1
    if value > 0: #only add if a link exists
        #add source and target to nodes list
        if not (source in tempNodes):
            nodeArr.append({"name":source,"group":getFromName(source)})
            tempNodes.append(source)
        if not (target in tempNodes):
            nodeArr.append({"name":target,"group":getFromName(target)})
            tempNodes.append(target)
        #add their links
        linksArr.append({"source":tempNodes.index(source),"target":tempNodes.index(target),"value":value})

with open("nodeLink_followers.json","w") as outfile:
    json.dump({"nodes":nodeArr,"links":linksArr},outfile,indent=4)