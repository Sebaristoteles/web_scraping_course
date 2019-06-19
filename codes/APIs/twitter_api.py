
import tweepy
import json
import pprint
from twitter_auth import auth
from twitter_datetime import datetime_parser


def get_tweets(api, screen_name):
    # Get user_timeline from twitter API
    tweets_json = [status._json for status in tweepy.Cursor(
        api.user_timeline,
        screen_name=screen_name,
        tweet_mode='extended'
    ).items(2)]
    return tweets_json


api = tweepy.API(auth)
tweets = get_tweets(api, '@guardian')

datajsondump = json.dumps(tweets)
datajson = json.loads(datajsondump, object_hook=datetime_parser)

pprint.pprint(datajson)
