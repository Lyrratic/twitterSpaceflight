import json
import io

ESA = ["astro_Jfrancois", "astro_timpeake", "Thom_astro", "Astro_Alex", "AstroSamantha", "astro_luca", "astro_andre", "astro_paolo", "Astro_Andreas", "CFuglesang", "ESA_EAC", "esa", "esaoperations"]
JAXA = ["Astro_Satoshi", "Astro_Wakata", "Astro_Soichi", "Astro_Kimiya", "JAXA_en", "Aki_Hoshide"]
CSA = ["csa_asc", "asc_csa", "Astro_Jeremy", "Astro_DavidS", "AstroDaveMD", "Cmdr_Hadfield", "RobertThirsk", "AstroGarneau"]
CSAExtra = ["RobertaBondar"]
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

def getFromName(mem):
    if mem in ESA: return 1
    if mem in JAXA: return 2
    if mem in CSA: return 3
    if mem in Roscosmos: return 4
    if mem in NASA: return 5

#Create the array of nodes:
nodeArr = []
tempNodes = []
#loop through all the group member's files and count replies+retweets,
#create links array
linksArr = []
groupIndex= 1
nodeIndex = 0
for groupN in groups:
    g = getGroup(groupN)
    for member in g:
        # memIndex = allAstro.index(member)
        allRepRet = [] #list of all members replied or retweeted to by the current member
        for line in open("../1215-415_data/" + member + "_users_replied.csv"):
            fixLine = line.replace("\n", "")
            allRepRet.append(fixLine)
        for line in open("../1215-415_data/" + member + "_users_retweeted.csv"):
            fixLine = line.replace("\n", "")
            allRepRet.append(fixLine)
        #print allRepRet
        for person in allRepRet:
            if person in allAstro:
                nodeFilter = filter(lambda thing: thing['name'] == member, nodeArr)
                if nodeFilter == [] :
                    print "adding",member
                    nodeArr.append({"name":member,"group":groupIndex})
                    tempNodes.append(member)
                nodeFilter2 = filter(lambda thing: thing['name'] == person, nodeArr)
                if nodeFilter2 == [] :
                    print "adding",person
                    nodeArr.append({"name":person,"group":getFromName(person)})
                    tempNodes.append(person)
                first = filter(lambda thing: thing['source'] == tempNodes.index(member), linksArr)
                second = filter(lambda thing2: thing2['target']== tempNodes.index(person), first)
                if second == []:
                    toAdd = {"source":tempNodes.index(member),"target":tempNodes.index(person),"value":1}
                    #print toAdd
                    linksArr.append(toAdd)
                    
                else:
                    second[0]["value"]+=1

        #{"source":1,"target":0,"value":1}
    groupIndex+=1

# for i in linksArr:
#     if i["source"] in tempNodes:
#         if i["target"] in tempNodes:
#             print "lol already here",i["target"]
#         else:
#             tempNodes.append(i["target"])
#     else:
#         tempNodes.append(i["source"])

# for node in tempNodes:
#     nodeArr.append({"name":allAstro[node],"group":getFromName(allAstro[node])})

with open("testOutput.json","w") as outfile:
    json.dump({"nodes":nodeArr,"links":linksArr},outfile,indent=4)