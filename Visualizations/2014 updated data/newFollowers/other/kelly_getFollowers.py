import time
import io
import tweepy

CONSUMER_KEY = 'lyI0jZEbPLJK1mPLYsgIrlsTG'
CONSUMER_SECRET = 'IfyrTRwIqSgV95Zl14UQsBa9ChPeohW9eSI7sWABxX23cki8Ee'
OAUTH_TOKEN = '2977560412-Rmf2FiRzkSDUNvwAUs5Qx6EDEj0kxcDquzhcgOL'
OAUTH_SECRET = 'SlWuglWaX2d2LD4nSnHUXr50bb2CS1Juck8UcThhwPOTK'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)

api = tweepy.API(auth)

NASA = [
"fka_roscosmos", "spacetihon", "AntonAstrey"
]
#account = "Astro_Nicole"

for account in NASA:
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