import redis
import json
import hashlib


#function that takes in rafflename, userid, and return all tweets

def RtrnTweet(raffle_name, user_name):
    r = redis.StrictRedis(host='ec2-34-198-54-21.compute-1.amazonaws.com', port=14779, db=0,
                          password='pd4f481dd62ae68b6068f2009a7f7a8d5e1e9cfc5a59d1fdce40ea09342818faa')

    return r.hgetall(raffle_name + ':' + user_name)

#returns all raffles
def RtnUsers(raffle_name):
    r = redis.StrictRedis(host='ec2-34-198-54-21.compute-1.amazonaws.com', port=14779, db=0,
                          password='pd4f481dd62ae68b6068f2009a7f7a8d5e1e9cfc5a59d1fdce40ea09342818faa')


    return r.lrange(raffle_name, 0, -1)

#returns all users in raffle
def RtnRaffles():
    r = redis.StrictRedis(host='ec2-34-198-54-21.compute-1.amazonaws.com', port=14779, db=0,
                          password='pd4f481dd62ae68b6068f2009a7f7a8d5e1e9cfc5a59d1fdce40ea09342818faa')
    return r.hgetall('raffle')

raffles = RtnRaffles()
print(raffles)

for raffle_name, raffle_info in raffles.items():
    print(raffle_info)
    users = RtnUsers(raffle_name)
    print(users)
    for user in users:
        user = json.loads(user)
        print(RtrnTweet(raffle_name.decode('utf-8'), user['username']))
