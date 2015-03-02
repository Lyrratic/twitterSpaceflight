import time
import io
import tweepy

CONSUMER_KEY = '1lVR14Vjd8QRt8YLaAJ8IquVK'
CONSUMER_SECRET = 'RYGSvSAgAAUsuF1BScaOxtorPLJH7B1WreCH2D0tKfrlK02Nld'
OAUTH_TOKEN = '2977560412-LPlpsE7AvOgulxB1O7lKYDayb9Z9xUeqIKr8q0g'
OAUTH_SECRET = 'FMogyNvQLjExbbmgTCIaoPixCqmRHvpUsaB6cVzBGao1J'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)

api = tweepy.API(auth)

accounts = ["astro_Jfrancois", "Thom_astro", "Astro_Alex", "astro_luca", "astro_andre", "Astro_Andreas", "CFuglesang", "ESA_EAC", "esaoperations",
"Astro_Satoshi", "Astro_Wakata", "JAXA_en", "Aki_Hoshide",
"asc_csa", "Astro_DavidS", "AstroDaveMD", "Cmdr_Hadfield", "RobertaBondar", "RobertThirsk", "AstroGarneau",
"fka_roscosmos", "spacetihon", "AntonAstrey"]

for account in accounts: 
	FOLLOWERS_FILE = account + "_followers.json"
	f = io.open(FOLLOWERS_FILE, 'w', encoding='utf8')

	ids = []
	for page in tweepy.Cursor(api.followers_ids, screen_name=account).pages():
	    ids.extend(page)
	    # print page
	    for follower in page:
	        f.write(unicode(str(follower) + '\n'))
	    time.sleep(60)
	    print len(ids)
	    print "  "

	print "total: "
	print len(ids)
	no_repeats = list(set(ids))
	print "With repeats removed: " + str(len(no_repeats))