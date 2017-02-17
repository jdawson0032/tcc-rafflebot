import hashlib
import json
import os

import redis


class RedisService():
    def __init__(self):
        self.client = redis.from_url(os.getenv('REDIS_URL', 'redis://localhost:6379'))
        self.raffles_key = 'raffles'

    # Gets the key where raffle users are stored
    def get_raffle_users_key(self, raffle_name):
        return raffle_name + ':users'

    # Gets the key where tweets for a user per raffle are stored
    def get_user_key(self, raffle_name, user_name):
        return raffle_name + ':' + user_name

    # Gets the key where account followers are stored
    def get_account_followers_key(self, account_name):
        return account_name + ':followers'

    # Gets if a user is following an account
    def is_user_following(self, account, user_id):
        return self.client.sismember(self.get_account_followers_key(account), user_id)

    # Sets the followers of an account
    def set_followers(self, account, followers=None):
        if followers is None:
            followers = []

        key = self.get_account_followers_key(account)

        self.client.delete(key)
        self.client.sadd(key, *followers)

    def add_post(self, raffle_name, post):
        username = post['user_name']
        text_hash = hashlib.md5(post['text'].encode()).hexdigest()

        self.client.sadd(self.get_raffle_users_key(raffle_name), username)
        self.client.hset(self.get_user_key(raffle_name, username), text_hash, json.dumps(post))

    def get_raffles(self):
        raffles = self.client.hgetall(self.raffles_key)
        output = {}
        for key, value in raffles.items():
            output[key.decode('utf-8')] = json.loads(value.decode('utf-8'))

        return output

    def get_users(self, raffle_name):
        users = self.client.smembers(raffle_name)
        output = []
        for user in users:
            output.append(json.loads(user))

        return output

    def get_posts(self, raffle_name, user_name):
        posts = self.client.hgetall(raffle_name + ':' + user_name)
        output = []
        for post in posts:
            output.append(json.load(post))

        return output

    def add_raffle(self, raffle):
        return self.client.hset(self.raffles_key, self.get_raffle_users_key(raffle.name), json.dumps(raffle.__dict__))
