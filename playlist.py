import json 
import pandas as pd
from config import client
import pprint
import random
import re
from unidecode import unidecode
from datetime import datetime
import sys

db = client.spotify

def save_playlist(selected_tracks, cluster):
    date = datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S")
    
    danceability = [track['danceability'] for track in selected_tracks]
    energy = [track['energy'] for track in selected_tracks]
    acousticness = [track['acousticness'] for track in selected_tracks]
    valence = [track['valence'] for track in selected_tracks]

    avg_danceability = sum(danceability)/len(danceability)
    avg_energy = sum(energy)/len(energy)
    avg_acousticness = sum(acousticness)/len(acousticness)
    avg_valence = sum(valence)/len(valence)

    playlist = {
        'playlist': selected_tracks,
        'name': 'Playlist - {}'.format(str(date)),       
        'avg_danceability':avg_danceability,
        'avg_energy':avg_energy,
        'avg_acousticness':avg_acousticness,
        'avg_valence':avg_valence,
        "created_at": date,
        'cluster_ref': cluster
    }

    print("Inserindo no banco de dados")
    db.playlists.insert_one(playlist)

def mount_playlist():
    for i in range(0,7):
        selected_tracks = []
        cluster = i

        cursor = db.tracks.find({'cluster':cluster})
        tracks = []
        used_rands = []

        for track in cursor:
            tracks.append(track)

        for i in range(0,15):

            rand = random.randint(0,len(tracks)-1)

            if rand in used_rands:
                rand = random.randint(0,len(tracks)-1)
            
            selected = tracks[rand]
            
            selected = {
                'id':selected['id'],
                'name':selected['name'],
                'album':selected['album']['name'],
                'artist': ', '.join([artist['name'] for artist in selected['artists']]),
                'popularity': selected['popularity'],
                'danceability':selected['audio_features']['danceability'],
                'energy':selected['audio_features']['energy'],
                'acousticness':selected['audio_features']['acousticness'],
                'valence':selected['audio_features']['valence']
            }

            selected_tracks.append(selected)

            used_rands.append(rand)
        # salva a playlist no banco de dados
        save_playlist(selected_tracks, cluster)

if __name__=='__main__':
    playlist = mount_playlist()