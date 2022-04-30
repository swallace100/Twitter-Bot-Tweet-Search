# Import Twitter API Tweepy. Complete API documentation is at https://docs.tweepy.org/en/stable/index.html
import tweepy

# Add API Key, API Key Secret, Bearer Token, Access Token and Access Token Secret from the Twitter Developer website
# Sign up for a Twitter Developer account at https://developer.twitter.com/ if you don't already have oe
API_KEY = 'ADD API KEY HERE'
API_KEY_SECRET = 'ADD API KEY SECRET HERE'

BEARER_TOKEN = 'ADD BEARER TOKEN HERE'

ACCESS_TOKEN = 'ADD ACCESS TOKEN HERE'
ACCESS_TOKEN_SECRET = 'ADD ACCESS TOKEN SECRET HERE'

VPS_DIRECTORY = '/twitterBot/data'


# This program returns all mentions of a Twitter username in a given timeframe. Twitter Essential Developer access
# only allows for 10 maximum tweets returned per search. Please adjust search timeframe as needed to make sure all the
# tweets you are looking for are returned.

# Class for getting a user's mentions. Creating this as a class allows the user to search multiple usernames at once.
class PostATweet(object):
    def __init__(self):
        self.client = tweepy.Client(BEARER_TOKEN, API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Change the search start time as needed.
    def get_mentions(self, id, username):
        user = username
        tweets = self.client.get_users_mentions(id, start_time='2021-12-01T00:00:00Z')

        print(f'Mentions for {user} are below.')
        print(tweets)


# Function that starts the search. Add the account userID and the account username for the search.
# Add more objects to allow for more searches.
if __name__ == '__main__':
    t = PostATweet()
    t.get_mentions(309366491, 'Twitch')

    print('')

    h = PostATweet()
    h.get_mentions(117652722, 'Hideo_Kojima_En')

    print('')

    o = PostATweet()
    o.get_mentions(14075928, 'TheOnion')




