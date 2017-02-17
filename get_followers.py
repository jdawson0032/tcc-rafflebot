import time

import twitter

from rafflebot.services.redis_service import RedisService

poll_delay = 60  # every minute
lastRun = 0

redis_service = RedisService()

if len(redis_service.get_raffles()) == 0:
    start = time.time()
    end = start + 60 * 60 * 4
    raffle = {
        'name': 'Sample Raffle',
        'start': start,
        'end': end,
        'account': 'DomEnterprises',
        'hashtags': [
            'hacku5'
        ]
    }
    redis_service.add_raffle(raffle)

api = twitter.Api(
    consumer_key='bwJeji4clbvJu1HweDNOTRtti',
    consumer_secret='3eO15Gt46MiEhVSqPP7tydtdL3SpKioKAo5W3xWnihIohQIooj',
    access_token_key='240143891-RNi9z3mmBcpnf0usafnQXZiJxegRv7AgVkYhNtit',
    access_token_secret='jpFL7tT6eeG3oz6NgM1Ks5Nzo9zN0tFJWoIdhISLMYK94'
)

while True:
    now = time.time()

    if lastRun + poll_delay <= now:
        raffles = redis_service.get_raffles()
        print(raffles)

        for raffle in raffles:
            account_name = raffle['account']
            followerIDs = api.GetFollowerIDs(screen_name=account_name)
            redis_service.set_followers(account_name, followerIDs)
            print('Found ' + str(len(followerIDs)) + ' followers for ' + account_name)

        lastRun = now
    else:
        time.sleep(1)
