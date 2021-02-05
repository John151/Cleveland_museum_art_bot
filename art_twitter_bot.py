"""bot to retrieve data from Cleveland museum of art API"""

import requests
import json
import random

def get_openaccess_results(medium, skip=0, limit=100):
    url = 'https://openaccess-api.clevelandart.org/api/artworks/'
    params = {
        'm': medium,
        'skip': skip,
        'limit': limit,
        'has_image': 1
    }
    data = requests.get(url, params=params).json()

    for artwork in data['data']:
        tombstone = artwork['tombstone']
        image = artwork['images']['web']['url']

        print(f"{tombstone}\n{image}\n---")

if __name__ == '__main__':
    get_openaccess_results("painting", 0, 10)