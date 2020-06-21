from pymongo import MongoClient

url = "https://api.spotify.com/v1/me/tracks?limit=50"
payload = {}
headers = {
  'Authorization': 'Bearer BQDmecV2qgzLQwVfIFkwet72G6JD4Ixn_7DT8YuBHX45zC_d_RgJ_DDt2D4O1pvlJZIeGYahezNyed4XcLq5wpIEl_6zdCl6wRc07xvua_A_iMrr1xGzCIDrQkDSmOqFOK8_F2TNVvuEYT2irEjyij78eYyBAyh_mnbO9zcbLm7dX3OfwCnVpzpN9ASdFVZa-U2CZn--euGWgktq3G8bWzbmu3J4dNUICbPxbXTx-PRpa9LGwi4HiPZpUXxRvA'
}

client = MongoClient('mongodb://localhost:27017/')

pitch_class = [
  {'0' :'C'},
  {'1' :'C#'},
  {'2' :'D'},
  {'3' :'D#'},
  {'4' :'E'},
  {'5' :'F'},
  {'6' :'F#'},
  {'7' :'G'},
  {'8' :'G#'},
  {'9' :'A'},
  {'10':'A#'},
  {'11':'B'}
]