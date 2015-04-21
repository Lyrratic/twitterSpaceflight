import json
import io

ESA = ["astro_Jfrancois", "astro_timpeake", "Thom_astro", "Astro_Alex", "AstroSamantha", "astro_luca", "astro_andre", "astro_paolo", "Astro_Andreas", "CFuglesang", "ESA_EAC", "esa", "esaoperations"]
JAXA = ["Astro_Satoshi", "Astro_Wakata", "Astro_Soichi", "Astro_Kimiya", "JAXA_en", "Aki_Hoshide"]
CSA = ["csa_asc", "asc_csa", "Astro_Jeremy", "Astro_DavidS", "AstroDaveMD", "Cmdr_Hadfield", "RobertaBondar", "RobertThirsk", "AstroGarneau"]
Roscosmos = ["fka_roscosmos", "spacetihon", "OlegMKS", "Msuraev", "AntonAstrey"]
NASA = ["NASA","NASA_Astronauts","NASAPeople","AstroClass2013","SciAstro","Astro_Flow","Astro_Cady","Astro_Ferg","AstroCoastie","astro_Pettit","AstroDot","Astro_Wheels","Astro_Doug","Astro_Taz","Astro_Box","Astro2fish","Astro_Jeff","AstroAcaba","AstroKarenN","Astro_Kate7","astro_kjell","Astro_127","AstroIronMike","foreman_mike","astro_aggie","AstroIllini","Astro_Mike","Astro_Nicholas","Astro_Nicole","astro_reid","Astro_Rex","AstroRM","Astro_Ron","Astro_Sandy","AstroSerena","StationCDRKelly","Astro_Maker","Astro_Suni","AstroTerry","astro_tim","AstroMarshburn","Astro_TJ","Chief_Astronaut","Commercial_Crew","DESERT_RATS","HMP","ISS_Research","NASAMightyEagle","NASA_NEEMO","NASA_Orion","PavilionLake","MorpheusLander","AstroRobonaut","NASA_SLS","Astro_Clay"]

groups = ["ESA", "JAXA", "CSA", "Roscosmos", "NASA"]
#groups=["Roscosmos"]
allAstro = ESA+JAXA+CSA+Roscosmos+NASA

def getGroup(group_name):
    if group_name == "ESA": return ESA 
    if group_name == "JAXA": return JAXA 
    if group_name == "CSA": return CSA 
    if group_name == "Roscosmos": return Roscosmos 
    if group_name == "NASA": return NASA 

#Create the array of nodes:
nodeArr = []
#loop through all the group member's files and count replies+retweets,
#create links array
linksArr = []
i = 1
for groupN in groups:
    g = getGroup(groupN)
    for member in g:
        memIndex = allAstro.index(member)
        nodeArr.append({"name":member,"group":i})
        allRepRet = [] #list of all members replied or retweeted to by the current member
        for line in open("../1215-415_data/" + member + "_users_replied.csv"):
            fixLine = line.replace("\n", "")
            allRepRet.append(fixLine)
        for line in open("../1215-415_data/" + member + "_users_retweeted.csv"):
            fixLine = line.replace("\n", "")
            allRepRet.append(fixLine)
        print allRepRet
        for person in allRepRet:
            if person in allAstro:
                first = filter(lambda thing: thing['source'] == memIndex, linksArr)
                second = filter(lambda thing2: thing2['target']==allAstro.index(person), first)
                if second == []:
                    toAdd = {"source":memIndex,"target":allAstro.index(person),"value":1}
                    print toAdd
                    linksArr.append(toAdd)
                else:
                    second[0]["value"]+=1
        #{"source":1,"target":0,"value":1}
    i+=1

with open("testOutput.json","w") as outfile:
    json.dump({"nodes":nodeArr,"links":linksArr},outfile,indent=4)