import twitter
import json
import io
import time
from twitter import *

CONSUMER_KEY = 'ZcyrvJRoGiU1yoZbCkterzUI7'
CONSUMER_SECRET = 'bDsHY2VZOs3b0iSAL0dxC0csBAQO7TlpVxsS3BXIDPls8YTdY5'
OAUTH_TOKEN = '2977560412-Ma2BvuQkpvIPUiwimWbCl8ogG6GmoLnQGIMC7KG'
OAUTH_SECRET = 'Bn0FAWFgs1EFI4vYIwHcfos14sa4TOhzffocdKwXqMenA'

# auth
t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

# user_data = t.users.show(screen_name="spacetihon")
# print user_data


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


name = "Aki_Hoshide"
a = Account(name)
objectJSON = a.jsonable()
print objectJSON
