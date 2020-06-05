import numpy as np
import pandas as pd
from pymongo import MongoClient
from config import client

db = client.spotify
cursor_tracks = db.tracks.find()
tracks = []
for track in cursor_tracks:
    track = {
        'name': track['name'],
        'durantion_ms': (track['duration_ms']/60000),
        'explicit': track['explicit'],
        'added_at': track['added_at'],
        'album': track['album']['name'],
        'release_date': track['album']['release_date'],
        'artist_id': ','.join([artist['id'] for artist in track['artists']]),
        'audio_features': track['audio_features']
    }

    tracks.append(track)

df_tracks = pd.json_normalize(tracks)
df_tracks.to_csv('tracks.csv',sep=';',index=False)

cursor_artists = db.artists.find()
artists = []
for artist in cursor_artists:
    artist = {
        'id': artist['id'],
        'artist_name': artist['name'],
        'artist_popularity': artist['popularity'],
        'artist_followers': artist['followers'],
        'artist_genres': ','.join(genre for genre in artist['genres'])
    }
    artists.append(artist)

df_artists = pd.json_normalize(artists)
df_artists.to_csv('artists.csv',sep=';',index=False)