"""bot to retrieve data from Cleveland museum of art API"""

import requests
import json
import random
import tweepy
import time

# store our credentials
def twitter_api():
    CONSUMER_KEY = '' # 'your API key number here'
    CONSUMER_SECRET = '' # 'your API secret key number here'
    ACCESS_KEY = '' # 'your access token here'
    ACCESS_SECRET = '' # 'your access token secret here'

    # setting up out access to tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    # api object that interacts with twitter
    api = tweepy.API(auth)
    return api


def main():
    api = twitter_api()
    results = get_openaccess_results("painting", 0, 100)
    image, tombstone = unpack(results)
    make_tweet(api, image, tombstone)

# this function calls the Cleveland Museum open API and gets results
def get_openaccess_results(medium, skip=0, limit=100):
    url = 'https://openaccess-api.clevelandart.org/api/artworks/?'
    params = {
        'q': medium,
        'skip': skip,
        'limit': limit,
        'has_image': 1
    }
    results = requests.get(url, params=params).json()
    return results

# this function unpacks the results we got from the api
# and chooses one at random
def unpack(results):

    random_painting = random.randint(0, 100)
    artwork = results['data'][random_painting]
    tombstone = artwork['tombstone']
    image = artwork['images']['web']['url']
    return image, tombstone
    print(f"{tombstone}\n{image}\n---")


def make_tweet(api, image, tombstone):
    temp_file = 'temp.jpg'
    url = image['url']
    request = requests.get(url, stream=True)
    if request.status_code == 200:
        with open(temp_file, 'wb') as painting
            for chunk in request:
                image.write(chunk)
        api.update_with_media(temp_file, status=tombstone)
        os.remove(temp_file)
    else:
        print("unable to download image")


if __name__ == '__main__':
    main()
