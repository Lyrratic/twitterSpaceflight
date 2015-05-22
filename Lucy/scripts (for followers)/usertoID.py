#converts users to ids
import time
import io
import tweepy
import csv
import json
import re
from datetime import datetime
from twitter import *

CONSUMER_KEY = 'Hqnlmc9MU8uekqrUl6FPXBkle'
CONSUMER_SECRET = 'KX7w9PKhoQBkr8doHri06WRRk4fPqrNwDdSV3YWeNvrfFKEyOZ'
OAUTH_TOKEN = '2815440649-pGpKHG8PPEkmCekQyU4LDooVaqNkMt0JvTCrq3G'
OAUTH_SECRET = 'wcTXAyEW7TyrWbluYAilRugkXmqKFhdbb2YzvML80ZY85'

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)
api = tweepy.API(auth)

#takes an array of usernames and converts to an array of IDs
def user_toID(userArray):
	userIDs = []
	for u in userArray:
		user = api.get_user(u)
		userIDs.extend([user.id])
		print u , str(user.id)
	return userIDs

ESA = user_toID(["astro_Jfrancois", "Thom_astro", "Astro_Alex", "AstroSamantha", "astro_luca", "astro_andre", "astro_paolo", "Astro_Andreas", "CFuglesang", "ESA_EAC", "esa", "esaoperations"])
JAXA = user_toID(["Astro_Satoshi", "Astro_Wakata", "Astro_Soichi", "Astro_Kimiya", "JAXA_en", "Aki_Hoshide"])
CSA = user_toID(["csa_asc", "asc_csa", "Astro_Jeremy", "Astro_DavidS", "AstroDaveMD", "Cmdr_Hadfield", "RobertaBondar", "RobertThirsk", "AstroGarneau"])
Roscosmos = user_toID(["fka_roscosmos", "spacetihon", "OlegMKS", "Msuraev", "AntonAstrey"])
NASA = user_toID(["NASA","NASA_Astronauts","NASAPeople","AstroClass2013","SciAstro","Astro_Flow","Astro_Cady","Astro_Ferg","AstroCoastie","astro_Pettit","AstroDot","Astro_Wheels","Astro_Doug","Astro_Taz","Astro_Box","Astro2fish","Astro_Jeff","AstroAcaba","AstroKarenN","Astro_Kate7","astro_kjell","Astro_127","AstroIronMike","foreman_mike","astro_aggie","AstroIllini","Astro_Mike","Astro_Nicholas","Astro_Nicole","astro_reid","Astro_Rex","AstroRM","Astro_Ron","Astro_Sandy","AstroSerena","StationCDRKelly","Astro_Maker","Astro_Suni","AstroTerry","astro_tim","AstroMarshburn","Astro_TJ","Chief_Astronaut","Commercial_Crew","DESERT_RATS","HMP","ISS_Research","NASAMightyEagle","NASA_NEEMO","NASA_Orion","PavilionLake","MorpheusLander","AstroRobonaut","NASA_SLS","Astro_Clay"])
missing = ["astro_timpeake"]

groups = ["ESA", "JAXA", "CSA", "Roscosmos", "NASA"]

def getGroup(group_name):
    if group_name == "ESA": return ESA 
    if group_name == "JAXA": return JAXA 
    if group_name == "CSA": return CSA 
    if group_name == "Roscosmos": return Roscosmos 
    if group_name == "NASA": return NASA 

#DO THE THIINNGGG
fout = open("astroAccountIDs.csv", "wb")
wr = csv.writer(fout, dialect='excel')

for g in groups:
	writing = [[g]+(getGroup(g))]
	wr.writerow(writing)