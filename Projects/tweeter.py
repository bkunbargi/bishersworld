import tweepy
import random

consumer_token = '578CqsXGvHGCEjVXGBEPlV3z3'
consumer_secret = 'Z1ZA6mexgpA6lSHVJTuvJ51X7xcmz2YiRsddfb3ztZNJzThOeP'
access_token = '956353285857845248-6LDp0wtcnIt3dKfeWwKhxIqVrwBAZMj'
access_token_secret = 'uk1FW7yG7D2yMJDQ1N9imeKGBJuPhA4NTZAVp8TMbigRP'

auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



def run_bot(input1, input2):
    goat_list = []
    result = tweepy.Cursor(api.search,q = input1, wait_on_rate_limit = True, tweet_mode = 'extended').items(100)
    for element in result:
        try:
            if(element.retweet_count == 0):
                tweet_text = element._json['full_text']
                if(input2 in (tweet_text)):
                    goat_list.append(tweet_text)
            else:
                tweet_text = element._json['retweeted_status']['full_text']
                if(input2 in (tweet_text)):
                    goat_list.append(tweet_text)
        except:
            pass

    goat_set = set(goat_list)
    return goat_set

def retweet(tweeted):
    try:
        api.update_status(str(tweeted))
        return tweeted
    except:
        return 'none'
