import tweepy
import random
import time
from textblob import TextBlob


consumer_token = '578CqsXGvHGCEjVXGBEPlV3z3'
consumer_secret = 'Z1ZA6mexgpA6lSHVJTuvJ51X7xcmz2YiRsddfb3ztZNJzThOeP'
access_token = '956353285857845248-6LDp0wtcnIt3dKfeWwKhxIqVrwBAZMj'
access_token_secret = 'uk1FW7yG7D2yMJDQ1N9imeKGBJuPhA4NTZAVp8TMbigRP'

auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)



def run_bot(input1):
    goat_list = list()
    print('Building Set')
    result = tweepy.Cursor(api.search,q = input1, lang = 'en', wait_on_rate_limit = True, tweet_mode = 'extended').items(100)
    time.sleep(1)
    for element in result:
        try:
            if(element.retweet_count == 0):
                tweet_text = element._json['full_text']
                goat_list.append(tweet_text)
            else:
                tweet_text = element._json['retweeted_status']['full_text']
                goat_list.append(tweet_text)
        except:
            pass

    return set(goat_list)


def run_analysis(tweeted_list):
    anaylsis_dict = dict()
    min_score = 0
    max_score = 0
    for tweet in tweeted_list:
        trating = TextBlob(tweet)
        anaylsis_dict[tweet] = trating.sentiment.polarity

    sorted_dic = sorted(anaylsis_dict.items(),key = lambda x:x[1])
    min_tweet,min_score = sorted_dic[0]
    max_tweet,max_score = sorted_dic[-1]

    min_tweet = min_tweet+' : Score({})'.format(min_score)
    max_tweet = max_tweet+' : Score({})'.format(max_score)

    try:
        api.update_status(min_tweet)
        time.sleep(1)
    except:
        pass
        #min_tweet = 'Lowest scored tweet not retrieved'
    try:
        api.update_status(max_tweet)
        time.sleep(1)
    except:
        pass
        #max_tweet = 'Max scored tweet not retrieved'

    return min_tweet,max_tweet
def retweet(content):
    api.update_status(content)
    return content
    
def respond_to(username,content,status_id):
    api.update_status(status = "@{} {}".format(username,content), in_reply_to_status_id = '{}'.format(status_id))
