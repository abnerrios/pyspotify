import requests
import json 
import pandas as pd
from multiprocessing import Pool
from config import payload, headers, client, pitch_class

db = client.spotify
# funções de inserção no mongo
def process_track(item):

  track = item['track']
  print('[+] Realizando parsing da faixa id: {}'.format(track['id']))
  # recupera informações adicionais
  audio_features = get_audio_features(track['id'])
  audio_features['key'] = pitch_class[audio_features['key']]
  # recupera apenas informações necessários do album
  album = {
    'id': track['album']['id'],
    'href':track['album']['href'],
    'name': track['album']['name'],
    'release_date': track['album']['release_date'],
    'external_urls': track['album']['external_urls']['spotify']
  }
  # recupera apenas informações importantes dos artistas
  artists = [{key: artist.pop(key,None) for key in ('id','href','name','external_urls')} for artist in track['artists']]
  # ajuste para que o registro contenha apenas as informações necessárias
    
  id = track['id']
  track = {
    'name': track['name'],
    'popularity': track['popularity'],
    'external_urls': track['external_urls'],
    'duration_ms': track['duration_ms'],
    'explicit': track['explicit'],
    'album': album,
    'cover': track['album']['images'][0],
    'artists': artists,
    'audio_features': audio_features,
    'added_at': item['added_at']
  }

  print('[+] Inserindo no mongodb')

  try:
    db.tracks.update({'id':id}, {'$set': track} , upsert=True)
    print('[+] Faixa salva com sucesso.')
  except:
    print('[+] Erro ao salvar faixa no banco de dados')

# funções de coleta de dados
def get_audio_features(id):
  url = 'https://api.spotify.com/v1/audio-features/{}'.format(id)
  response = requests.request('GET', url, headers=headers, data = payload)
  # joga o resultado para a variável 
  audio_features = json.loads(response.content)

  return audio_features

def get_tracks():
  url = 'https://api.spotify.com/v1/me/tracks?limit=50'

  while True:
    # faz chamada na api até que todas as faixas sejam retornadas
    response = requests.request('GET', url, headers=headers, data = payload)
    content = json.loads(response.content)
    tracks = content['items']
    # executa a chamada do processamento em multiprocessos
    with Pool(5) as p:
      p.map(process_track, tracks)

    # utiliza o valor retornado para paginação
    url = content['next'] 
    if not url:
      break
    
    print(url)
    
  return True 

def insert_artist(id, artist):
  try:
    db = client.spotify
    db.artists.update({'id':id}, {'$set': artist} , upsert=True)
    print('[+] Artista salvo com sucesso.')
  except:
    print('[+] Erro ao salvar artista no banco de dados')

def get_artists():
  cursor = db.tracks.distinct('artists.id')

  for artist_id in cursor:
    url = 'https://api.spotify.com/v1/artists/{}'.format(artist_id)
    response = requests.request('GET', url, headers=headers, data = payload)
    artist = json.loads(response.content)

    artist = {
      'id':artist['id'],  
      'name': artist['name'],
      'popularity': artist['popularity'],
      'genres':artist['genres'],
      'image':artist['images'],
      'followers':artist['followers']['total'],
      'external_urls':artist['external_urls']['spotify']
    }

    insert_artist(artist_id, artist)

  return True

if __name__=='__main__':
  on_get_tracks = get_tracks()
  on_get_artists = get_artists()