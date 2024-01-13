import os
from pymongo import MongoClient
from pyxportify import Api
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")
spotify = Api(authorization_token=token)
mongohost = os.getenv("MONGODB_HOST")
mongoport = int(os.getenv("MONGODB_PORT"))
mongo = MongoClient(f"mongodb://{mongohost}:{mongoport}/")
db = mongo.spotify


def get_library_tracks():
    offset = 0
    limit = 20
    while True:
        tracks = spotify.library.tracks(limit=limit, offset=offset)
        tracks_id = [track.get("track").get("id") for track in tracks]

        for track in tracks:
            track_id = track.get("track").get("id")
            db.tracks.find_one_and_update(
                {"track.id": track_id}, {"$set": track}, upsert=True
            )

        audio_features_list = spotify.tracks.audio_features(
            track_id=None, ids=tracks_id
        )

        for audio_features in audio_features_list.get("audio_features"):
            db.tracks.find_one_and_update(
                {"track.id": audio_features.get("id")},
                {"$set": {"audio_features": audio_features}},
                upsert=False,
            )

        offset += limit
        if len(tracks) < limit:
            break


if __name__ == "__main__":
    get_library_tracks()
