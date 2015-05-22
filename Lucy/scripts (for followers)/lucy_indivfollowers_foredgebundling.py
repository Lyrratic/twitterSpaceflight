import io
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

ESA_names = ["astro_Jfrancois", "astro_timpeake", "Thom_astro", "Astro_Alex", "AstroSamantha", "astro_luca", "astro_andre", "astro_paolo", "Astro_Andreas", "CFuglesang", "ESA_EAC", "esa", "esaoperations"]
JAXA_names = ["Astro_Satoshi", "Astro_Wakata", "Astro_Soichi", "Astro_Kimiya", "JAXA_en", "Aki_Hoshide"]
CSA_names = ["csa_asc", "asc_csa", "Astro_Jeremy", "Astro_DavidS", "AstroDaveMD", "Cmdr_Hadfield", "RobertaBondar", "RobertThirsk", "AstroGarneau"]
Roscosmos_names = ["fka_roscosmos", "spacetihon", "OlegMKS", "Msuraev", "AntonAstrey"]
NASA_names = ["NASA","NASA_Astronauts","NASAPeople","AstroClass2013","SciAstro","Astro_Flow","Astro_Cady","Astro_Ferg","AstroCoastie","astro_Pettit","AstroDot","Astro_Wheels","Astro_Doug","Astro_Taz","Astro_Box","Astro2fish","Astro_Jeff","AstroAcaba","AstroKarenN","Astro_Kate7","astro_kjell","Astro_127","AstroIronMike","foreman_mike","astro_aggie","AstroIllini","Astro_Mike","Astro_Nicholas","Astro_Nicole","astro_reid","Astro_Rex","AstroRM","Astro_Ron","Astro_Sandy","AstroSerena","StationCDRKelly","Astro_Maker","Astro_Suni","AstroTerry","astro_tim","AstroMarshburn","Astro_TJ","Chief_Astronaut","Commercial_Crew","DESERT_RATS","HMP","ISS_Research","NASAMightyEagle","NASA_NEEMO","NASA_Orion","PavilionLake","MorpheusLander","AstroRobonaut","NASA_SLS","Astro_Clay"]

everyone = ESA_names+JAXA_names+CSA_names+Roscosmos_names+NASA_names
everyoneID = ESA + JAXA + CSA + Roscosmos + NASA
groups = ["ESA", "JAXA", "CSA", "Roscosmos", "NASA"]
groups_names = ["ESA_names", "JAXA_names", "CSA_names", "Roscosmos_names", "NASA_names"]

def getGroupArray(group_name):
    if group_name == "ESA": return ESA 
    if group_name == "JAXA": return JAXA 
    if group_name == "CSA": return CSA 
    if group_name == "Roscosmos": return Roscosmos 
    if group_name == "NASA": return NASA 

def getGroup(account):
    if account in ESA:
        print account + "ESA" 
        return "ESA" 
    if account in JAXA: 
        print account + "JAXA" 
        return  "JAXA" 
    if account in CSA: 
        print account + "CSA" 
        return  "CSA" 
    if account in Roscosmos: 
        print account + "Roscosmos" 
        return  "Roscosmos" 
    if account in NASA: 
        print account + "NASA" 
        return  "NASA" 

#DO THE THIINNGGG
fout = csv.writer(open("followerLinks.csv", "wb"))
# source, target, following, followed by

pairs = []

for i in range (0,len(everyone)):
    source = everyone[i]
    sourceID = everyoneID[i]
    sourceFollowers = []
    # targetFollowers = []
    # following = "False"
    # followedBy = "False"
    sourceFollowers.extend(line.strip() for line in open("../"+source+'_followers.json'))
    for k in range (int(i+1),len(everyone)):
        following = "False"
        followedBy = "False"
        targetFollowers = []
        target = everyone[k]
        targetID = everyoneID[k]
        print "linking: ",source,target
        # pairs.append([everyone[i],everyone[k]])
        targetFollowers.extend(line.strip() for line in open("../"+target+'_followers.json'))
        if str(targetID) in sourceFollowers:
            followedBy = "True"
        if str(sourceID) in targetFollowers:
            following = "True"
        fout.writerow([source,target,following,followedBy])