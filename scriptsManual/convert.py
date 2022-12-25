import json
import csv

# Import json
with open('/mnt/c/users/weice/Desktop/spotifyAPI/data/playlistData.json') as jsonFile:
    data = json.load(jsonFile)
    column_names = ["name", "danceability", "energy", "key", "loudness", "mode", "speechiness", "acousticness", "instrumentalness",
        "liveness", "valence", "tempo", "type", "id", "uri", "track_href", "analysis_url", "duration_ms", "time_signature"]
    data_lst = []
    for key in data:
        row = [key]
        row.extend(data[key].values())
        data_lst.append(row)
    
    filename = "/mnt/c/users/weice/Desktop/spotifyAPI/scripts/rawData.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(column_names)
        csvwriter.writerows(data_lst)
#https://www.geeksforgeeks.org/convert-json-to-csv-in-python/