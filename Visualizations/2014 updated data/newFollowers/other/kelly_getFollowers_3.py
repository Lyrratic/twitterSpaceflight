import time
import io
import tweepy

CONSUMER_KEY = 'U2J5Q8BR5e2WrfyEcVocWS4Og'
CONSUMER_SECRET = 'wMmUkRyzxxzrUnD0GpUlkc79NfvcUuXDt1aFdZoU2IsFeXZkGT'
OAUTH_TOKEN = '2977560412-9RvZ6N6sfI5FlwKMo4n1GVGEaZsMXkeG97EsZt0'
OAUTH_SECRET = 'YzhTiJgA47SwGqw0FBFtZArsteBN9aQfS0EwDd4DtJOTA'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)

api = tweepy.API(auth)

#account = "Astro_Wheels"
NASA = [
"Astro_Mike",
]

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