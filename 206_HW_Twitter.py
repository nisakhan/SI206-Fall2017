import unittest
import tweepy
import requests
import json

## SI 206 - HW
## COMMENT WITH:
## Nisa Khan
## Your section day/time: Thursdays 3-4
## Any names of people you worked with on this assignment: Got help from Ilma Bilic


## Write code that uses the tweepy library to search for tweets with three different phrases of the
## user's choice (should use the Python input function), and prints out the Tweet text and the
## created_at value (note that this will be in GMT time) of the first FIVE tweets with at least
## 1 blank line in between each of them, e.g.


## You should cache all of the data from this exercise in a file, and submit the cache file
## along with your assignment.

## So, for example, if you submit your assignment files, and you have already searched for tweets
## about "rock climbing", when we run your code, the code should use CACHED data, and should not
## need to make any new request to the Twitter API.  But if, for instance, you have never
## searched for "bicycles" before you submitted your final files, then if we enter "bicycles"
## when we run your code, it _should_ make a request to the Twitter API.

## Because it is dependent on user input, there are no unit tests for this -- we will
## run your assignments in a batch to grade them!

## We've provided some starter code below, like what is in the class tweepy examples.

##SAMPLE OUTPUT
## See: https://docs.google.com/a/umich.edu/document/d/1o8CWsdO2aRT7iUz9okiCHCVgU5x_FyZkabu2l9qwkf8/edit?usp=sharing



## **** For extra credit, create another file called twitter_info.py that
## contains your consumer_key, consumer_secret, access_token, and access_token_secret,
## import that file here.  Do NOT add and commit that file to a public GitHub repository.

## **** If you choose not to do that, we strongly advise using authentication information
## for an 'extra' Twitter account you make just for this class, and not your personal
## account, because it's not ideal to share your authentication information for a real
## account that you use frequently.

## Get your secret values to authenticate to Twitter. You may replace each of these
## with variables rather than filling in the empty strings if you choose to do the secure way
## for EC points
consumer_key = "TMsbGZML5iwPtPqYIFlktBSZO"
consumer_secret = "duLMmk0Y0WfNhbbO0ZfH8rzlCo9ybizHK2R2KE9t7mgzB5awbq"
access_token = "920735606958886912-1Dj7G8j9qjFsGfkUANFYzrH2pJQq1eu"
access_token_secret = "PoLp1P5fI4zRXe5BGvAEyqyTDzxPhpDrezOvDzjpTxdGX"
## Set up your authentication to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# Set up library to grab stuff from twitter with your authentication, and
# return it in a JSON-formatted way

api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

## Write the rest of your code here!

#### Recommended order of tasks: ####
## 1. Set up the caching pattern start -- the dictionary and the try/except
## 		statement shown in class.

CACHE_FNAME = "cache_tweet_info.json" #Creating a string

try:
    fo = open(CACHE_FNAME, "r") #open file
    cache_contents = fo.read() #read
    CACHE_DICTION = json.loads(cache_contents)
    fo.close()
    # my_posts_raw = fo.read() #into a string
    # posts_in_json = json.loads(my_posts_raw)
    # fo.close() #close
except:
    CACHE_DICTION = {} #empty
    # post_in_json = {} #empty


## 2. Write a function to get twitter data that works with the caching pattern,
## 		so it either gets new data or caches data, depending upon what the input
##		to search for is.

def get_t(search_term):
    data = json.loads(search_term)
    print(data) #print search terms

## 3. Using a loop, invoke your function, save the return value in a variable, and explore the
##		data you got back!


## 4. With what you learn from the data -- e.g. how exactly to find the
##		text of each tweet in the big nested structure -- write code to print out
## 		content from 5 tweets, as shown in the linked example.

def getTwitterWithCaching(search_term):
    full_url = "twitter_{}".format(search_term)
    if full_url in CACHE_DICTION:
        print("Data in cache")
        print("\n")
        return CACHE_DICTION[full_url]
    else:
        twitter_result = api.search(q = full_url, count = 5)
        try:
            CACHE_DICTION[full_url] = twitter_result #passing results into full_urls
            cache_tweet_info = json.dumps(CACHE_DICTION) #passing in data into json file
            fo = open(CACHE_FNAME, "w")
            fo.write(cache_tweet_info) #write to the file
            fo.close() #closed
            return CACHE_DICTION[full_url]
        except:
            print("Not in cache")
            return None

for i in range(3):
    search_term = input("Enter Tweet term: ") #entering keywords
    twitter_result = getTwitterWithCaching(search_term)
    for r in twitter_result["statuses"][:5]:
        ##  going through texts, priting out tweets
        print("TEXT:", r["text"])
        print("CREATED AT:", r["created_at"])
        print("\n")
