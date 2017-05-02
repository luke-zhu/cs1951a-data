import json
import numpy as np

with open('data/metacritic_albums.json') as albums_file:
    albums = json.load(albums_file)

artists = {}

for album in albums:
    if album['artist'] in artists:
        artists[album['artist']].append(album)
    else:
        artists[album['artist']] = [album]

with open('data/metacritic_avgs.json', 'w') as outfile:
    avg_scores = []
    for artist, albums in artists.items():
        avg_scores.append([artist, np.mean([int(album['score']) for album in albums])])
    json.dump(avg_scores, outfile)