import json
import io
import pymongo
import tweepy
import csv

from pymongo import MongoClient
client = MongoClient()
db = client.tweetsAnalysis
collection = db.tweets

CONSUMER_KEY = '1lVR14Vjd8QRt8YLaAJ8IquVK'
CONSUMER_SECRET = 'RYGSvSAgAAUsuF1BScaOxtorPLJH7B1WreCH2D0tKfrlK02Nld'
ACCESS_KEY = '2977560412-LPlpsE7AvOgulxB1O7lKYDayb9Z9xUeqIKr8q0g'
ACCESS_SECRET = 'FMogyNvQLjExbbmgTCIaoPixCqmRHvpUsaB6cVzBGao1J'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.secure = True
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)

def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	
	pass

if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("NASA_SLS")

