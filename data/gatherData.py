import json
import pandas as pd
import requests

# we're gonna use our three playlists This is Niki, This is Anson Seabra, and This is Joji to do a test run
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#playlist features class
class Song: 
  def __init__(self, name, uri, artistName, package):
    self.name = name
    self.uri = uri
    self.artist = artistName
    self.package = package

    
songs = []
trackUris = []

# get all the data from the playlist, and add it to "list" of songs
def getPlayList(playlistURL, songList):
    
    playlistUri = playlistURL.split("/")[-1].split("?")[0]
    curPlaylistUris = [x["track"]["uri"] for x in sp.playlist_tracks(playlistUri)["items"]]
    trackUris.append(curPlaylistUris) # each playlist in the track is being recorded as a trackUri
    
    
    #run through this for loop:
    for s in sp.playlist_tracks(playlistUri)["items"]:
        trackUri = s["track"]["uri"]
        trackName = s["track"]["name"]
        artistName = s["track"]["artists"][0]["name"]
        pack = sp.audio_features(trackUri)[0]
        song = Song(trackName, trackUri, artistName, pack)
        songList.append(song)

# change everything to JSON
# turn json Song List into a JSON File
def getJSONFile(songList):
    #TODO: implement
    masterDick = {}
    for i in range(len(songList)):
        masterDick[songList[i].name + " *by* " + songList[i].artist] = songList[i].package
    with open("playlistData.json", "w") as outfile:
        json.dump(masterDick, outfile, indent = 4)
         
def printSongs():
    for song in songs:
        print("-----------------------")
        print(song.name)
        print(song.uri)
        print(song.artist)

def printSongFeatures():
    for song in songs:
        print("-----------------------")
        print(song.package)
    
    

if __name__ == "__main__": #main
    #first we want to extrat data from the song class
    #keep getting the songs until use desides not to past in URL anymore
    #Authentication - without user
    cid = 'b2714d0ebea740edb51613c004bbfa6c'#input("enter your id: ")
    secret = '2b7bd29633944b19a52becd985b8ccfe'#input("enter your secret: ")
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)
    q = False
    while(1):
        plink = input("enter the playlist link: ")
        getPlayList(plink, songs)
        qq = input("quit? y for yes, n for no (case sensitive)") 
        if qq == 'y' or qq == 'yes':
            q = True
        if q:
            break
    # verify our song features, our playlists, and get our json file
    # printSongs()
    # printSongFeatures()
    getJSONFile(songs)
