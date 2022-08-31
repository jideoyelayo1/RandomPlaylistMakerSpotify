import random
import string
import urllib.parse
import requests


class SpotifyClient(object):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_random_tracks(self, TOKEN):
        wildcard = f'%{random.choice(string.ascii_lowercase)}%'
        query = urllib.parse.quote(wildcard)
        offset = random.randint(0, 2000)

        url = f'https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track'

        response = requests.get(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {TOKEN}"
            }
        )
        response_json = response.json()
        print(response_json)

        tracks = [track for track in response_json['tracks']['items']]
        print(f"found {len(tracks)} from your search")

        return tracks

    def add_tracks_to_library(self, track_ids):
        url = 'https://api.spotify.com/v1/me/tracks'

        response = requests.put(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}"
            },
            json={
                'ids': track_ids
            }
        )
        return response.ok

    def add_tracks_to_playlist(self, track_ids, playlist_id, ADD_TO_PLAYLIST_TOKEN):
        url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

        response = requests.post(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {ADD_TO_PLAYLIST_TOKEN}"
            },
            json={
                'uris': track_ids
            }
        )
        return response.ok

    def create_a_playlist(self, user_id, TOKEN, PlaylistName):
        url = f'https://api.spotify.com/v1/users/{user_id}/playlists'

        response = requests.post(
            url,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {TOKEN}"
            },
            json={
                "name": PlaylistName,
                "description": "Made with a spotify API",
                "public": False
            }
        )
        response_json = response.json()
        #print(response_json)
        #print("the ", response_json['id'], " playlist has been made")

        return response_json['id']
