import tweepy, csv
consumer_key='K0cvlhlshR7SS4PVk6smJZqxG'
consumer_secret='oCFV2iP3Nv1GxgahMIJbDoboFmCtLAFJXNB70e4lh3bwbu9IH7'
access_token='1090590791750148096-6NuhCD8Lov29OQaE9UJpeQiTwX93iJ'
access_token_secret='zO0JpF1LaXw3S09l6QndSMQOkRqI2mWgmUUNXHCa0otob'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
api.verify_credentials()

    
#search = api.search(q="Pune", lang="en", rpp=100,count=100)

# for tweet in search:
#    # printing the text stored inside the tweet object
#    print(tweet.user.screen_name,"Tweeted:",tweet.text.encode('ascii','ignore'))  

file_out = open("tweets2.csv","w+",encoding="utf-8")

writer = csv.writer(file_out, delimiter=",",quotechar='"', quoting=csv.QUOTE_MINIMAL)

i=0
#AES Acute Encephalitis Syndrome
for item in tweepy.Cursor(api.search, q="Encephalitis Syndrome").items(10):
    i+=1
    print("adding item",i,item.id)
    tweet = []
    tweet.append(item.created_at)
    tweet.append(item.user.screen_name)
    tweet.append(item.text)
    tweet.append(item.entities)
    writer.writerow(tweet)

file_out.close()    


