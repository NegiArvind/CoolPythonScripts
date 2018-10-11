# -*- coding: utf-8 -*-

# This Script will give you the positive result or negative result percentage about some topic by
# analysing twitter sentiments

# Import libraries
from textblob import TextBlob  #This library is used to determine whether a sentence is positve or negative
# Value is ranges from -1 to +1 . -1 means negative review,+1 positive review and 0 means neutral
import tweepy # tweepy is used to deal with twitter api
import matplotlib.pyplot as plt


def percentage(part,whole):
    return 100*float(part)/float(whole)

consumer_key="3qwQ4u9AWTXAdiGb2RplDhQVA"
consumer_secret_key="eA11rsh3tgqcNi0uZ6g48ByUGW77AuVz2vRWimgfxTxAudmUJ3"
access_token="898928030361333760-yKR5Micneta8LV0Lv3aEgdOteYz2bVr"
access_secret_token="IzR0P9oGiZDJC9MFiS8fpzgEhqOytVkrtSR9pPKEsTy9s"

# Authentication
auth=tweepy.OAuthHandler(consumer_key=consumer_key,consumer_secret=consumer_secret_key)
auth.set_access_token(access_token,access_secret_token)
api=tweepy.API(auth)

searchTerm=input("Enter keyword/hashtag to search about: ")
noOfSearchTerms=int(input("Enter no. of tweets to anaylyze: "))

tweets=tweepy.Cursor(api.search,q=searchTerm,lang='en').items(noOfSearchTerms) # it will return you the specified no. of 
# tweets onto your search topic.


positive=0
negative=0
neutral=0
polarity=0

for tweet in tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text) # it will anaylize the tweet(check whether it is positive ,negative or neutral)
    tweetPolarity=analysis.sentiment.polarity # return value ranges between -1 to +1.
    polarity+=tweetPolarity
    
    if tweetPolarity==0.00:
        neutral+=1
    elif tweetPolarity<0.00:
        negative+=1
    elif tweetPolarity>0.00:
        positive+=1
        
positive=percentage(positive,noOfSearchTerms)
negative=percentage(negative,noOfSearchTerms)
neutral=percentage(neutral,noOfSearchTerms)


# Formatting upto 2 decimal
positive=format(positive,'.2f')
negative=format(negative,'.2f')
neutral=format(neutral,'.2f')

print("\nHow people are reacting on "+searchTerm+" by analyzing "+str(noOfSearchTerms)+ " tweets.")

if(polarity==0.00):
    print("Neutral")
elif polarity<0.00:
    print("Negative")
elif polarity>0.00:
    print("Positive")
    
# Drawing a pie chart
    
labels=['Positive ['+str(positive)+'%]','Neutral ['+str(neutral)+'%]','Negative ['+str(negative)+'%]']
colors=['green','yellow','red']
sizes=[positive,neutral,negative]
patches,texts=plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc='best')
plt.title("How people are reacting on "+searchTerm+" by analyzing "+str(noOfSearchTerms)+ "tweets.")
plt.axis('equal')
plt.tight_layout()
plt.show()

