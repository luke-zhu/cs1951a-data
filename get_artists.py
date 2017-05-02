import json

with open('data/top_songs_2013-06-22.json') as file1:
    data = json.load(file1)

with open('data/top_songs_2015-05-30.json') as file2:
    data += json.load(file2)

with open('data/top_songs_2017-05-06.json') as file3:
    data += json.load(file3)

artists = set()
for song in data:
    if 'Featuring' in song['artist']:
        artists.add(song['artist'].split(' Featuring')[0])
    elif 'Featuing' in song['artist']:
        artists.add(song['artist'].split(' Featuing')[0])
    elif 'Featruing' in song['artist']:
        artists.add(song['artist'].split(' Featruing')[0])
    elif 'Feat.' in song['artist']:
        artists.add(song['artist'].split(' Feat.')[0])
    else:
        artists.add(song['artist'].split(', ')[0])

with open('data/billboard_artists.json', 'w') as outfile:
    json.dump(list(artists), outfile)