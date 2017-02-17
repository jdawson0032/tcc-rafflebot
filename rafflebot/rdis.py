#Service app J.Dawson
#17 Feb 2017
import redis
import json



class raffbt(object):
    def __init__(self):
        self.client = redis.StrictRedis(host='ec2-34-198-54-21.compute-1.amazonaws.com', port=14779, db=0,
                                        password='pd4f481dd62ae68b6068f2009a7f7a8d5e1e9cfc5a59d1fdce40ea09342818faa')
        pass

    # function that takes in rafflename, userid, and return all tweets
    def RtrnTweet(self, raffle_name, user_name):
        return self.client.hgetall(raffle_name + ':' + user_name)

    # returns all raffles
    def RtnUsers(self, raffle_name):
        return self.client.lrange(raffle_name, 0, -1)

    # returns all users in raffle
    def RtnRaffles(self):
        return self.client.hgetall('raffle')


bot = raffbt()

raffles = bot.RtnRaffles()
print(raffles)

for raffle_name, raffle_info in raffles.items():
    print(raffle_info)
    users = bot.RtnUsers(raffle_name)
    print(users)
    for user in users:
        user = json.loads(user)
        print(bot.RtrnTweet(raffle_name.decode('utf-8'), user['username']))


# create a raffle
    def raffCreate(raffleName, userName, userTweet):
        r = redis.StrictRedis(host='ec2-34-198-54-21.compute-1.amazonaws.com', port=14779, db=0,
                      password='pd4f481dd62ae68b6068f2009a7f7a8d5e1e9cfc5a59d1fdce40ea09342818faa')
        raffle = {'name': raffleName, 'username': userName, 'tweet': userTweet}
        r.hset('raffle', raffleName, json.dumps('raffle'))
    def createCache(username, user_follower):
        r= redis.StrictRedis(host = 'ec2-34-198-54-21.compute-1.amazonaws.com', port=14779, db=0,
                      password='pd4f481dd62ae68b6068f2009a7f7a8d5e1e9cfc5a59d1fdce40ea09342818faa')
        r.sadd(username + ':followers', *user_follower))
    def checkList(username, userfollower):
         r = redis.StrictRedis(host='ec2-34-198-54-21.compute-1.amazonaws.com', port=14779, db=0,
                               password='pd4f481dd62ae68b6068f2009a7f7a8d5e1e9cfc5a59d1fdce40ea09342818faa')
         r.sadd(username + ':followers', userfollower)
