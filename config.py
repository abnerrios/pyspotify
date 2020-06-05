from pymongo import MongoClient

url = "https://api.spotify.com/v1/me/tracks?limit=50"
payload = {}
headers = {
  'Authorization': 'Bearer BQAgPmm_TEs1CROi15MqJnBKh4_6TzpIN5DJLdierTdISZLGpdSLJNOwz_jHxvxs5hE7517pyInTFDDEVlsvZ3uH0cSfs2XKlgaT1UcmpCtKyLwPzJbNpyV7g7TvLuhBImmEfsSMpTIlAOtMeZtMuu-6RxBTDmskSs8XkSrzrI6lPngX5BnHQlxnKQgoEdKj2hviP9LRn5788VUKhQkVk6IU8I5o0zZRpQz9FuerTV6W_I2hLWw'
}

client = MongoClient('mongodb://localhost:27017/')

pitch_class = [
  {'key':0, 'label':'C'},
  {'key':1, 'label':'C#'},
  {'key':2, 'label':'D'},
  {'key':3, 'label':'D#'},
  {'key':4, 'label':'E'},
  {'key':5, 'label':'F'},
  {'key':6, 'label':'F#'},
  {'key':7, 'label':'G'},
  {'key':8, 'label':'G#'},
  {'key':9, 'label':'A'},
  {'key':10, 'label':'A#'},
  {'key':11, 'label':'B'}
]