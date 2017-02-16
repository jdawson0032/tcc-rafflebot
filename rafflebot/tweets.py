'''

import tweepy

auth = tweepy.OAuthHandler('RmWG8S047ag7YP8Xb5RyrlEsV', '0oCy3JoernuZqUQ3FAJDzsT3OaFPaDX0XJbJYyo767eQnUGRvk')
auth.set_access_token('109412756-QWkzI8GQC38epLvxDDs2WCoGlswADszmpLDzzQXh', '021TcodQnsD8UEmLMi3L9MUlTf8jKCHqfTaFSieLULvqC')

api = tweepy.API(auth)


api = twitter.Api(consumer_key='RmWG8S047ag7YP8Xb5RyrlEsV',
                     consumer_secret='0oCy3JoernuZqUQ3FAJDzsT3OaFPaDX0XJbJYyo767eQnUGRvk',
                     access_token_key='109412756-QWkzI8GQC38epLvxDDs2WCoGlswADszmpLDzzQXh',
                     access_token_secret='021TcodQnsD8UEmLMi3L9MUlTf8jKCHqfTaFSieLULvqC')
'''

import twitter

#dom_followers = get_dom_follers()

api = twitter.Api(consumer_key='QUGnrBWzjkNJUiDtHASHCcsYX',
                      consumer_secret='YE9mTQqOk2GmBqVObNLmzTztIstNrIuig5lvjIb30H7beAoKLR',
                      access_token_key='109412756-QWOKm1kskbRUFhkp8zlNMLQDVMvVCS3H7iGBw4YV',
                      access_token_secret='yN570u2QFzrWWhp0iPso0wmLjDWMv0uv3PlIIHgGX5QUB')

'''
results = api.GetSearch(
    raw_query="q=%23HACKU5%20&result_type=recent&since=2014-07-19&count=10")  # get the users with hashtag
'''
results = api.GetSearch(
    raw_query="q=%23HACKU5%20&result_type=recent&since=2014-07-19")  # get the users with hashtag

sender='Monster_Clean'
users = [elem.AsDict()['user']['id'] for elem in results] # and extract their user id's
print (type(users))

domfols = api.GetFollowerIDs(screen_name='DomEnterprises')  # get user id's of users following DomEnterprises

for user in users:
    if user in domfols:
        print (user)
    else:
        print ('Fail')

'''

domfollowers = api.GetFollowerIDs('@DomEnterprises')
print (domfollowers)
print([u.name for u in users])


print (domfollowers)

 Now work with Twitter
 print(api.VerifyCredentials())
'''