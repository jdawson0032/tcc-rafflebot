import time
import twitter
import hashlib

from rafflebot.services.redis_service import RedisService


def get_stream(streams, raffle):
    name = raffle['name']
    if name not in streams:
        api = twitter.Api(
            consumer_key='bwJeji4clbvJu1HweDNOTRtti',
            consumer_secret='3eO15Gt46MiEhVSqPP7tydtdL3SpKioKAo5W3xWnihIohQIooj',
            access_token_key='240143891-RNi9z3mmBcpnf0usafnQXZiJxegRv7AgVkYhNtit',
            access_token_secret='jpFL7tT6eeG3oz6NgM1Ks5Nzo9zN0tFJWoIdhISLMYK94'
        )

        tracking = raffle['account']

        for tag in raffle['hashtags']:
            tracking += ' ' + tag

        streams[name] = api.GetStreamFilter(track=[tracking])

    return streams[name]


redis_service = RedisService()

streams = {}

raffles = redis_service.get_raffles()

def has_appropriate_entities(mentions, hashtags, raffle):
    has_mention = False
    has_hashtags = False

    for mention in mentions:
        has_mention = has_mention or mention['screen_name'] == raffle['account']

    for tag in hashtags:
        has_hashtags = has_hashtags or tag in hashtags

    return has_mention and has_hashtags


def handle_post(redis_service, raffle, post):
    mentions = post['entities']['user_mentions']
    hashtags = post['entities']['hashtags']

    if not has_appropriate_entities(mentions, hashtags, raffle):
        return

    user_id = post['user']['id']

    if not redis_service.is_user_following(raffle['account'], user_id):
        return

    screen_name = post['user']['screen_name']
    text = post['text']

    redis_service.add_post(raffle['name'], {'user_name': screen_name, 'user_id': user_id, 'text': text})


handle_post(
    redis_service,
    {
        'name': 'Sample Raffle',
        'start': time.time(),
        'end': time.time() + 6000,
        'account': 'DomEnterprises',
        'hashtags': [
            'hacku5'
        ]
    },
    {'in_reply_to_screen_name': None, 'id_str': '832393258256969728', 'created_at': 'Fri Feb 17 00:56:32 +0000 2017', 'source': '<a href="http://twitter.com" rel="nofollow">Twitter Web Client</a>', 'lang': 'en', 'id': 832393258256969728, 'retweeted': False, 'text': 'Testing an app here, hope it works this time @DomEnterprises  and STILL enjoying the learnin.  #hacku5', 'in_reply_to_status_id_str': None, 'timestamp_ms': '1487292992544', 'filter_level': 'low', 'coordinates': None, 'contributors': None, 'entities': {'urls': [], 'user_mentions': [{'name': 'Dominion Enterprises', 'screen_name': 'DomEnterprises', 'id_str': '35935371', 'id': 35935371, 'indices': [45, 60]}], 'hashtags': [{'text': 'hacku5', 'indices': [95, 102]}], 'symbols': []}, 'favorited': False, 'favorite_count': 0, 'is_quote_status': False, 'in_reply_to_status_id': None, 'truncated': False, 'retweet_count': 0, 'in_reply_to_user_id_str': None, 'geo': None, 'in_reply_to_user_id': None, 'place': None, 'user': {'profile_image_url': 'http://pbs.twimg.com/profile_images/378800000624907720/6ebcac12626e21db7543fed0b9a8a357_normal.png', 'profile_sidebar_border_color': 'C0DEED', 'id_str': '109412756', 'geo_enabled': True, 'default_profile_image': False, 'statuses_count': 125, 'friends_count': 141, 'lang': 'en', 'followers_count': 211, 'is_translator': False, 'verified': False, 'profile_banner_url': 'https://pbs.twimg.com/profile_banners/109412756/1381289871', 'following': None, 'profile_sidebar_fill_color': 'DDEEF6', 'notifications': None, 'created_at': 'Thu Jan 28 23:57:26 +0000 2010', 'profile_background_color': 'C0DEED', 'contributors_enabled': False, 'location': 'Virginia Beach, VA', 'profile_link_color': '1DA1F2', 'profile_background_tile': False, 'favourites_count': 8, 'default_profile': True, 'description': 'Carpet, Oriental Rug, Tile and Upholstery Cleaning', 'screen_name': 'Monster_Clean', 'id': 109412756, 'listed_count': 0, 'profile_background_image_url_https': 'https://abs.twimg.com/images/themes/theme1/bg.png', 'time_zone': 'Eastern Time (US & Canada)', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/378800000624907720/6ebcac12626e21db7543fed0b9a8a357_normal.png', 'follow_request_sent': None, 'profile_text_color': '333333', 'protected': False, 'profile_background_image_url': 'http://abs.twimg.com/images/themes/theme1/bg.png', 'name': 'James Stallings', 'utc_offset': -18000, 'url': 'http://www.monsterclean.com', 'profile_use_background_image': True}}
)

# for raffle_name, raffle in raffles.items():
#     stream = get_stream(streams, raffle)
#     for post in stream:
#         handle_post(redis_service, raffle, post)
