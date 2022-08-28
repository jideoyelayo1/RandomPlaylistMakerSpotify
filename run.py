import os
from spotify_client import SpotifyClient


def run():
    # search for rnd songs
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
    random_track = spotify_client.get_random_tracks()
    track_ids = [track['id'] for track in random_track]
    # add rnd of rnd to lib
    was_added_to_library = spotify_client.add_tracks_to_library(track_ids)
    if was_added_to_library:
        for track in random_track:
            print(f"Added{track['name']} to your library")


if __name__ == '__main__':
    run()
