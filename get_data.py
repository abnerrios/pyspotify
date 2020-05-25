import requests
import json 
import pandas as pd
from config import payload, headers, client

def insert_track(id, track):
  try:
    db = client.spotify
    db.tracks.update({'id':id}, {'$set': track} , upsert=True)
    print('[+] Faixa salva com sucesso.')
  except:
    print('[+] Erro ao salvar faixa no banco de dados')

def get_audio_features(id):
  url = url = 'https://api.spotify.com/v1/audio-features/{}'.format(id)
  response = requests.request('GET', url, headers=headers, data = payload)
  # joga o resultado para a variável 
  audio_features = json.loads(response.content)

  return audio_features

def get_tracks():
  tracks = []
  url = url = 'https://api.spotify.com/v1/me/tracks?limit=50'

  while True:
    response = requests.request('GET', url, headers=headers, data = payload)
    content = json.loads(response.content)
    # faz chamada na api até que todas as faixas sejam retornadas
    for item in content['items']:
      track = item['track']
      print('[+] Realizando parsing da faixa id: {}'.format(track['id']))
      # recupera informações adicionais
      audio_features = get_audio_features(track['id'])
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
        'artists': artists,
        'audio_features': audio_features,
        'added_at': item['added_at']
      }

      print('[+] Inserindo no mongodb')
      # insere no banco de dados
      insert_track(id, track)
    
    # utiliza o valor retornado para paginação
    url = content['next'] 
    if not url:
      break
    print(url)
  

if __name__=='__main__':
  on_get_tracks = get_tracks()