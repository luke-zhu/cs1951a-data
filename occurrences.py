import json

with open('data/posts-top.json', 'r') as post_file:
    posts = json.load(post_file)

with open('data/billboard_artists.json', 'r') as artist_file:
    artists = json.load(artist_file)

occurrences = {}

for post in posts:
    for artist in artists:
        if artist in post['title']:
            if artist in occurrences:
                occurrences[artist] += 1
            else:
                occurrences[artist] = 1

with open('occurrences-top.json', 'w') as outfile:
    filtered_occurences = sorted([(k, v) for k, v in occurrences.items() if v >= 2],
        key=lambda x: -x[1])
    json.dump(filtered_occurences, outfile)
