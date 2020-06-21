import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from pymongo import MongoClient
from config import client

db = client.spotify
cursor = db.tracks.find()
tracks = []

for track in cursor:
    track = {
        'id':track['id'],
        'name':track['name'],
        'album':track['album']['name'],
        'artist': [artist['name'] for artist in track['artists']],
        'popularity': track['popularity'],
        'danceability':track['audio_features']['danceability'],
        'energy':track['audio_features']['energy'],
        'acousticness':track['audio_features']['acousticness'],
        'valence':track['audio_features']['valence']
    }
    tracks.append(track)

df_tracks = pd.json_normalize(tracks)

audio_features = df_tracks[['danceability','energy','acousticness','valence']]

# Padroniza a escala dos campos
X_scaled = StandardScaler().fit_transform(audio_features)

# define a quantidade de clusters
n = 4
kmeans = KMeans(n_clusters=n)

# Aplica o modelo
labels = kmeans.fit_predict(X_scaled)
# verifica o balanceamento dos clusters
label, count = np.unique(labels, return_counts=True)
for l, c in zip(label,count):
    print('Cluster {}: {}'.format(l,c))

df_tracks = df_tracks.join(pd.DataFrame(labels, columns=['cluster']))

# Atualiza o cluster no mongodb
client = MongoClient('mongodb://localhost:27017/')
db = client.spotify

for track in df_tracks.itertuples():
    update = {'cluster':track.cluster}
    db.tracks.update_one({'id':track.id},{"$set": update}, upsert=False)