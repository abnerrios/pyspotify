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
        'name': 'Automatic Playlist - {}'.format(str(date)),       
        'avg_danceability':avg_danceability,
        'avg_energy':avg_energy,
        'avg_acousticness':avg_acousticness,
        'avg_valence':avg_valence,
        "created_at": date,
        'cluster_ref': cluster
    }

    print("Inserindo no banco de dados")
    db.playlists.insert_one(playlist)


def next_track(key, cluster):
    cursor = db.tracks.find({'cluster':cluster, 'name':{'$regex':'^{}'.format(key)}})
    tracks = []
    # cria uma lista com as possíveis músicas
    for track in cursor:
        tracks.append(track)
    # seleciona uma faixa aleatória
    if len(tracks)==0:
        return "Finished"

    i = random.randint(0,len(tracks)-1)
    selected = tracks[i]
    next_key = unidecode(selected['name'][-1].upper())

    # verifica se o último caracter é uma letra
    if re.match(r'[A-Z]',next_key):
        print(selected['name'])
        print("Segue para próxima faixa.")
    else:
        # seleciona uma faixa aleatória
        i = random.randint(0,len(tracks)-1)
        selected = tracks[i]
        next_key = unidecode(selected['name'][-1].upper())

    # Retorna alguns campos apenas    
    selected = {
        'id':selected['id'],
        'name':selected['name'],
        'album':selected['album']['name'],
        'artist': [artist['name'] for artist in selected['artists']],
        'popularity': selected['popularity'],
        'danceability':selected['audio_features']['danceability'],
        'energy':selected['audio_features']['energy'],
        'acousticness':selected['audio_features']['acousticness'],
        'valence':selected['audio_features']['valence']
    } 
    return selected

def mount_playlist():
    selected_tracks = []
    cluster = 2
    # inicia a procurando músicas com a letra abaixo
    selected = next_track('K', cluster)

    # salva a playlist no banco de dados e encerra caso não encontra música com a letra
    if selected == "Finished":
        if len(selected)<=4:
            sys.exit()
        else:
            save_playlist(selected_tracks, cluster)
            sys.exit()
    # elimina conjunto de caracteres que não fazem parte do titulo da musica
    title = re.sub(r'- .*|\[.*\]|\(.*\)','',selected['name']).strip()
    key = unidecode(title[-1].upper())
    selected_tracks.append(selected)

    for i in range(0,13):
        selected = next_track(key, cluster)

        if selected=='Finished':
            save_playlist(selected_tracks, cluster)
            sys.exit()

        if selected['id'] in [track['id'] for track in selected_tracks]:
            i = 1
            while selected['id'] in [track['id'] for track in selected_tracks]:
                selected = next_track(key, cluster)
                if i >=3:
                    save_playlist(selected_tracks, cluster)
                    sys.exit()
                i+=1
        # descobre a última letra dessa música
        title = re.sub(r'- .*|\[.*\]|\(.*\)','',selected['name']).strip()
        key = unidecode(title[-1].upper())
        selected_tracks.append(selected)
    # salva a playlist no banco de dados
    save_playlist(selected_tracks, cluster)

if __name__=='__main__':
    playlist = mount_playlist()
