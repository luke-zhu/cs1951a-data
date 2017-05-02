import json

with open('data/billboard_artists.json', 'r') as artists_file:
    artists = json.load(artists_file)

"""
with open('data/top_songs_2013-06-22.json') as file1:
    data = json.load(file1)

with open('data/top_songs_2015-05-30.json') as file2:
    data += json.load(file2)

with open('data/top_songs_2017-05-06.json') as file3:
    data += json.load(file3)
"""

with open('data/billboard_albums.json') as infile:
    data = json.load(infile)


occurrences = {}

for artist in artists:
    occurrences[artist] = set()

for album in data:
    for artist in artists:
        if artist in album['artist']:
            occurrences[artist].add(album['week'])

with open('data/album_weeks-unique.json', 'w') as outfile:
    filtered_occurrences = sorted([(k, len(v)) for k, v in occurrences.items() if len(v) >= 10],
        key=lambda x: -x[1])
    json.dump(filtered_occurrences, outfile)
