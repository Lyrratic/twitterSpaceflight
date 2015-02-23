import json
import io
import time
from twitter import *
from json import dumps, load

CONSUMER_KEY = 'Hqnlmc9MU8uekqrUl6FPXBkle'
CONSUMER_SECRET = 'KX7w9PKhoQBkr8doHri06WRRk4fPqrNwDdSV3YWeNvrfFKEyOZ'
OAUTH_TOKEN = '2815440649-pGpKHG8PPEkmCekQyU4LDooVaqNkMt0JvTCrq3G'
OAUTH_SECRET = 'wcTXAyEW7TyrWbluYAilRugkXmqKFhdbb2YzvML80ZY85'

# auth
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

# user_data = t.users.show(screen_name="spacetihon")
# print user_data

#all the users:
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


class Account:

    def __init__(self, name): #makes 1 call to users
        self.screen_name = name

        #get user_data
        # throttle("USER_SHOW_THROTTLE")
        self.user_data = t.users.show(screen_name=name)

        self.name = self.user_data["name"] #name
        self.id = self.user_data["id"] #id
        self.profile_image = self.user_data["profile_image_url"] #profile_image
        self.location = self.user_data["location"] #location
        self.description = self.user_data["description"] #description
        self.created_at = self.user_data["created_at"] #creation of account
        
        self.followers_count = self.user_data["followers_count"] #number of followers
        self.following_count = self.user_data["friends_count"] #number of following
        self.tweets_count = self.user_data["statuses_count"] #number of tweets
        self.favorites_count = self.user_data["favourites_count"] #number of favorites

    def jsonable(self):
        return json.dumps(self.__dict__, ensure_ascii=False)


#name = "Aki_Hoshide"
"""name = "Aki_Hoshide"
a = Account(name)
objectJSON = a.jsonable()
print objectJSON

#open and write the json files
with io.open(name+'.txt', 'w', encoding='utf-8') as f:
  f.write(unicode(objectJSON))"""

for acc in JAXA:
    name = acc
    a = Account(name)
    objectJSON = a.jsonable()
    with io.open(name+'.txt', 'w', encoding='utf-8') as f:
        f.write(unicode(objectJSON))
    print "wrote file for: " + name