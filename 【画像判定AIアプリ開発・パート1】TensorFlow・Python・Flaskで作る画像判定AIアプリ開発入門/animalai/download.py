from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

# API Key
key  = '4f3d86e71d4c5545405dea3f0b0d06cd'
secret = '356c5d0421ef9969'
wait_time = 1

# 保存フォルダの指定
animalname = sys.argv[1]
savedir = './' + animalname

flickr = FlickrAPI(key, secret, format='parsed-json')
result = flickr.photos.search(
    text = animalname,
    per_page = 400,
    media = 'photos',
    sort = 'relevance', #関連順
    safe_search = 1, # UIコンテンツは表示しない
    extras = 'url_q, licence'
)

#pprint(result)
photos = result['photos']
#pprint(photos)

for i, photo in enumerate(photos['photo']):
    url_q = photo['url_q']
    filepath = savedir + '/' + photo['id'] + '.jpg'
    if os.path.exists(filepath): continue
    urlretrieve(url_q, filepath)
    time.sleep(wait_time)
