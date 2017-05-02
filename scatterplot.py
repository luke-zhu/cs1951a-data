import json

with open('data/metacritic_avgs.json') as metacritic_file:
    metacritic_scores = json.load(metacritic_file)

with open('data/artist_sentiments.json') as genius_file:
    genius_sentiments = json.load(genius_file)


scatterplot_data = []

for x in metacritic_scores:
    artist_m = x[0]
    for y in genius_sentiments:
        artist_g = y[0]
        if artist_m.lower() == artist_g.lower():
            scatterplot_data.append({
                'artist': x[0].lower(),
                'avg_score': x[1],
                'num_albums': x[2],
                'sentiment': y[1],
            })

with open('data/scatterplot_data3.json', 'w') as outfile:
    json.dump(scatterplot_data, outfile)
