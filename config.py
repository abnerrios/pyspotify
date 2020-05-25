from pymongo import MongoClient

url = "https://api.spotify.com/v1/me/tracks?limit=50"
payload = {}
headers = {
  'Authorization': 'Bearer BQBJpQf3qrNVpE6knYi3aKZRaC1PXs26nnhNQ4ca_hGHKHMB_9ZgGRAoPuZ5BdqypGqiH4_cUl-JD8ae0RTy8KJrtcMh9tvOjWCuQyGgvnmm9uSvtJSx-_p9SePbcu44fTExLsQMrUijT2fUbM5y3VkCv0NKlXBSyHShi1r_GxpOzYwvRmjcymt7NdANyXcVzvFwMrSPRKWmw71fJOIYIn7QD5CmrEhtALZLv0qCMt2yiIJrP0o'
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