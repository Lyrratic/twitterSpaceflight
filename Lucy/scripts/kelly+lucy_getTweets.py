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

ESA = ["astro_Jfrancois", "astro_timpeake", "Thom_astro", "Astro_Alex", "AstroSamantha", "astro_luca", "astro_andre", "astro_paolo", "Astro_Andreas", "CFuglesang", "ESA_EAC", "esa", "esaoperations"]
JAXA = ["Astro_Satoshi", "Astro_Wakata", "Astro_Soichi", "Astro_Kimiya", "JAXA_en", "Aki_Hoshide"]
CSA = ["csa_asc", "asc_csa", "Astro_Jeremy", "Astro_DavidS", "AstroDaveMD", "Cmdr_Hadfield", "RobertaBondar", "RobertThirsk", "AstroGarneau"]
Roscosmos = ["fka_roscosmos", "spacetihon", "OlegMKS", "Msuraev", "AntonAstrey"]
NASA = ["NASA","NASA_Astronauts","NASAPeople","AstroClass2013","SciAstro","Astro_Flow","Astro_Cady","Astro_Ferg","Astro_Clay","AstroCoastie","astro_Pettit","AstroDot","Astro_Wheels","Astro_Doug","Astro_Taz","Astro_Box","Astro2fish","Astro_Jeff","AstroAcaba","AstroKarenN","Astro_Kate7","astro_kjell","Astro_127","AstroIronMike","foreman_mike","astro_aggie","AstroIllini","Astro_Mike","Astro_Nicholas","Astro_Nicole","astro_reid","Astro_Rex","AstroRM","Astro_Ron","Astro_Sandy","AstroSerena","StationCDRKelly","Astro_Maker","Astro_Suni","AstroTerry","astro_tim","AstroMarshburn","Astro_TJ","Chief_Astronaut","Commercial_Crew","DESERT_RATS","HMP","ISS_Research","NASAMightyEagle","NASA_NEEMO","NASA_Orion","PavilionLake"]
NASA2 = ["MorpheusLander","AstroRobonaut","NASA_SLS"]

groups = ["ESA", "JAXA", "CSA", "Roscosmos", "NASA"]

def getGroup(group_name):
    if group_name == "ESA": return ESA 
    if group_name == "JAXA": return JAXA 
    if group_name == "CSA": return CSA 
    if group_name == "Roscosmos": return Roscosmos 
    if group_name == "NASA": return NASA 

# file 1: name_tweets_summary
SUMMARY_FILE = "extra.txt"
f_summary = io.open(SUMMARY_FILE, 'w', encoding='utf8')
f_summary.write(unicode("account, group, totalTweets, totalRetweetedTweets, totalReplyTweets, totalMediaTweets, totalRetweets, totalFavorites\n"))


def get_all_tweets(screen_name, group_name):
    #Twitter only allows access to a users most recent 3240 tweets with this method

    #authorize twitter, initialize tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(OAUTH_TOKEN, OAUTH_SECRET)

    api = tweepy.API(auth)

    #initialize a list to hold all the tweepy Tweets
    alltweets = []	

    #make initial request for most recent tweets (200 is the maximum allowed count)
    new_tweets = api.user_timeline(screen_name = screen_name,count=200)
    print "new_tweets length: " + str(len(new_tweets))

    #save most recent tweets
    alltweets.extend(new_tweets)

    #save the id of the oldest tweet less one
    oldest = alltweets[-1].id - 1

    #keep grabbing tweets until there are no tweets left to grab
    while len(new_tweets) > 0:
        print "getting tweets before %s" % (oldest)

        try:
            #all subsiquent requests use the max_id param to prevent duplicates
            new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

            #save most recent tweets
            alltweets.extend(new_tweets)

            #update the id of the oldest tweet less one
            oldest = alltweets[-1].id - 1

            print "...%s tweets downloaded so far" % (len(alltweets))

        except tweepy.TweepError:
            print "*****hit the limit*****"
            for i in range(15):
                time.sleep(60)
                print str(i+1) + " minutes complete"
            print "done with pause, continuing"
            continue

    #transform the tweepy tweets into a 2D array that will populate the csv	
    #outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
    #write the csv	
    #with open('../%s_tweets.csv' % screen_name,  'w') as f:
        #writer = csv.writer(f)
        #writer.writerow(["id","created_at","text"])
        #writer.writerows(outtweets)

    #variables to fux with
    totalTweets = len(alltweets)
    totalRetweetedTweets = 0
    retweetedTweetsAccounts = []
    totalReplyTweets = 0
    replyTweetsAccounts = []
    totalMediaTweets = 0
    totalRetweets = 0
    totalFavorites = 0
    urls = []
    hashtags = []
    account = screen_name

    # file 6: name tweets-- tweet text, # of favorites, # of retweets
    file6 = "../"+account + '_tweets.csv'
    f6 = io.open(file6, 'w', encoding='utf8')
    f6.write(unicode('tweet,retweetsCount,favoritesCount,timestamp\n'))

    for tweet in alltweets:
        #print str(tweet.created_at)
        tweetDate = datetime.strptime(str(tweet.created_at), "%Y-%m-%d %H:%M:%S")
        beginDate = datetime(2014,1,1,0,0,0)
        endDate = datetime(2015,1,1,0,0,0)
        if ((tweetDate.date() > beginDate.date()) and (tweetDate.date() < endDate.date())):
            if tweet.text[:2]=="RT":
                splitting = re.split('@|:',tweet.text)
                totalRetweetedTweets = totalRetweetedTweets + 1 #increment tweets retweeted?
                retweetedTweetsAccounts.append(splitting[1]) #add to list of retweeted accounts
                #print splitting[1]
                if tweet.in_reply_to_screen_name != None: 
                    totalReplyTweets = totalReplyTweets + 1 #increment replies to?
                    replyTweetsAccounts.append(tweet.in_reply_to_screen_name) #add to list of replies
                if len(tweet.entities) == 5:
                    totalMediaTweets = totalMediaTweets + 1 #increment media content?
                if len(tweet.entities["urls"]) > 0:
                    for url in tweet.entities["urls"]:
                        urls.append(url["expanded_url"]) #add to urls
                    if len(tweet.entities["hashtags"]) > 0:
                        for hashtag in tweet.entities["hashtags"]:
                            hashtags.append(hashtag["text"]) #add to hashtags       
                            totalFavorites += tweet.favorite_count 
                            totalRetweets += tweet.retweet_count
                #output tweets to file
                f6.write(unicode('"' + tweet.text.replace('\n', ' ').replace('"', '\'') + '",' + str(tweet.retweet_count) + ',' + str(tweet.favorite_count) + ',' + str(tweet.created_at) + '\n'))


    # file 2: name list of users retweeted
    file2 = "../"+account + '_users_retweeted.csv'
    f2 = io.open(file2, 'w', encoding='utf8')
    for user in retweetedTweetsAccounts:
        f2.write(unicode(user + '\n'))
    # file 3: name list of users replied
    file3 = "../"+account + '_users_replied.csv'
    f3 = io.open(file3, 'w', encoding='utf8')
    for user in replyTweetsAccounts:
        f3.write(unicode(user + '\n'))
    # file 4: name list of hashtags
    file4 = "../"+account + '_hashtags.csv'
    f4 = io.open(file4, 'w', encoding='utf8')
    for h in hashtags:
        f4.write(unicode(h + '\n'))
    # file 5: name list of urls
    file5 = "../"+account + '_urls.csv'
    f5 = io.open(file5, 'w', encoding='utf8')
    for u in urls:
        f5.write(unicode(u + '\n'))
    #summary
    f_summary.write(unicode(account + ',' + group_name + ',' + str(totalTweets) + ',' + str(totalRetweetedTweets) + ',' + str(totalReplyTweets) + ',' + str(totalMediaTweets) + ',' + str(totalRetweets) + ',' + str(totalFavorites) + '\n'))

    pass

if __name__ == '__main__':
    #plug in the groups: ESA, JAXA, CSA, Roscosmos, NASA
    group = NASA2
    for account in group:
        print "======Currently getting: " + account
        #pass in the username of the account you want to download
        get_all_tweets(account,"NASA")