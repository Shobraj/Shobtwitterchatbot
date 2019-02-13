from tweepy import StreamListener, OAuthHandler, Stream, API
from credentials import Consumer_API_key, Consumer_API_secret_key, Access_token,Access_token_secret
import time 

FILE_NAME = 'id_file.txt'

#for the first time copy paste this id "1095726430493626369" in id_file

auth = OAuthHandler(Consumer_API_key, Consumer_API_secret_key)
auth.set_access_token(Access_token, Access_token_secret)

api = API(auth)

def retrive_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name,'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    


def reply_to_tweet():
    print('replying to tweet')
    last_seen_id = retrive_last_seen_id(FILE_NAME)

    public_tweets = api.mentions_timeline(last_seen_id, tweet_mode = 'extended')
    for tweet in reversed(public_tweets):
        print(str(tweet.id)+'-'+tweet.full_text)
        last_seen_id = tweet.id
        store_last_seen_id(last_seen_id, FILE_NAME)

        if '#chatbot_testing' in tweet.full_text.lower():
            print('#chatbot_testing found')
            print('respnding now ....')
            api.update_status('Hello @'+tweet.user.screen_name+' thanks for tweeting with #chatbot_testing', tweet.id)

while True:
    reply_to_tweet()
    time.sleep(10)



'''public_tweets = api.mentions_timeline()
for tweet in reversed(public_tweets):
    print(str(tweet.id)+'-'+tweet.text)
    last_seen_id = tweet.id
    #store_last_seen_id(last_seen_id, FILE_NAME)

    if '#chatbot_testing' in tweet.text.lower():
        print('#chatbot_testing found')
        print('respnding now ....')'''