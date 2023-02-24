import tweepy 
import csv
import pandas as pd
import matplotlib.pyplot as plt
import re
import seaborn as sns
from textblob import TextBlob
import numpy as np
from datetime import date, datetime, timedelta
plt.style.use('fivethirtyeight')


api_key = ' '
api_secret_key = ' '
accsess_token = ' '
accsess_token_secret = ' '

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(accsess_token, accsess_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
search_key = ['partai kebangkitan bangsa', 'PKB']

#list
list_date = []
list_user = []
list_user_mention = []
list_teks = []
list_like = []
list_reetwet = []
list_link = []
list_id = []

for teks_key in search_key:
    key = teks_key

    i = 1
    for tweet in tweepy.Cursor(api.search_tweets, q=key, count=1000, lang="in").items():
        tweet = tweet

        tweet_date = str(tweet.created_at)
        tweet_user = tweet.user.screen_name
        tweet_user_mention = tweet.in_reply_to_screen_name
        tweet_teks = tweet.text
        tweet_like = tweet.favorite_count
        tweet_rt = tweet.retweet_count
        tweet_link = "https://twitter.com/"+tweet.user.screen_name+"/status/"+tweet.id_str+"/"
        tweet_user_id = "#"+ tweet.user.id_str

        list_date.append(tweet_date)
        list_user.append(tweet_user)
        list_user_mention.append(tweet_user_mention)
        list_teks.append(tweet_teks)
        list_like.append(tweet_like)
        list_reetwet.append(tweet_rt)
        list_link.append(tweet_link)
        list_id.append(tweet_user_id)

    df = pd.DataFrame({
        'Tanggal': list_date,
        'User': list_user,
        'User/Mentions': list_user_mention,
        'Text/Comment':list_teks,
        'Likes': list_like,
        'Teetwet': list_reetwet,
        'Link': list_link,
        'Id': list_id,
    })

    df.drop_duplicates()
    df.to_csv(datetime.now().strftime("%d-%m-%Y") + 'pkb.xlsx', index=False, encoding='utf-8')

        

        
