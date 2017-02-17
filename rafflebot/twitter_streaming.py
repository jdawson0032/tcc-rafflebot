# import necessary package to process data in JSON format
import twitter
try:
    import json
except ImportError:
    import simplejson as json

#import the necessary methods from the twitter library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream# Import the necessary package to process data in JSON format
try:
    import json
except ImportError:
    import simplejson as json

# Import the necessary methods from "twitter" library
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN = 'QWOKm1kskbRUFhkp8zlNMLQDVMvVCS3H7iGBw4YV'
ACCESS_SECRET = 'yN570u2QFzrWWhp0iPso0wmLjDWMv0uv3PlIIHgGX5QUB'
CONSUMER_KEY = 'QUGnrBWzjkNJUiDtHASHCcsYX'
CONSUMER_SECRET = 'YE9mTQqOk2GmBqVObNLmzTztIstNrIuig5lvjIb30H7beAoKLR'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

# Initiate the connection to Twitter Streaming API
twitter_stream = TwitterStream(auth=oauth)

# Get a sample of the public data following through Twitter
iterator = twitter_stream.statuses.sample()

# Print each tweet in the stream to the screen111
tweet_count = 1000
for tweet in iterator:
    tweet_count -= 1
    # Twitter Python Tool wraps the data returned by Twitter
    # as a TwitterDictResponse object.
    # We convert it back to the JSON format to print/score
    print json.dumps(tweet)

    # The command below will do pretty printing for JSON data, try it out
    # print json.dumps(tweet, indent=4)

    if tweet_count <= 0:
        break