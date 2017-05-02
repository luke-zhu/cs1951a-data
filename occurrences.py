import json

with open('data/genius.json', 'r') as post_file:
        posts = json.load(post_file)

for i in range(2, 8):
    with open('data/genius{}.json'.format(i), 'r') as post_file:
        posts += json.load(post_file)

with open('data/billboard_artists.json', 'r') as artist_file:
    artists = json.load(artist_file)

occurrences = {}

for post in posts:
    for artist in artists:
        flag = True
        for word in artist.lower().split():
            if word not in post['title'].lower():
                flag = False
                break

        if flag:
            if artist in occurrences:
                occurrences[artist] += 1
            else:
                occurrences[artist] = 1

with open('genius_occurences.json', 'w') as outfile:
    filtered_occurences = sorted([(k, v) for k, v in occurrences.items() if v >= 10],
        key=lambda x: -x[1])
    json.dump(filtered_occurences, outfile)
