import json
import numpy as np

with open('data/sentiments.json', 'r') as post_file:
    posts = json.load(post_file)

with open('data/billboard_artists.json', 'r') as artist_file:
    artists = json.load(artist_file)

filtered_posts = []

for post in posts:
    if 'fresh' in post['url']:
        filtered_posts.append((post['url'], post['polarity']))

with open('data/album_sentiments.json', 'w') as outfile:
    json.dump(sorted(filtered_posts, key=lambda x: -x[1]), outfile)
