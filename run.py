import os
from spotify_client import SpotifyClient

Create_Playlist_TOKEN = open('TOKEN.txt', 'r').read()
PlaylistName = "RandomPlaylist"
ADD_TO_PLAYLIST_TOKEN = Create_Playlist_TOKEN
TOKEN = Create_Playlist_TOKEN

"""Create_Playlist_TOKEN = 
PlaylistName = "RandomPlaylist"
ADD_TO_PLAYLIST_TOKEN = 
TOKEN = """


def run():
    # search for rnd songs
    spotify_client = SpotifyClient(TOKEN)  # os.getenv('SPOTIFY_AUTH_TOKEN'))
    playlist_id = spotify_client.create_a_playlist(user_id="1176214954", TOKEN=Create_Playlist_TOKEN
                                                   , PlaylistName=PlaylistName)

    random_track = spotify_client.get_random_tracks(TOKEN=TOKEN)
    track_ids = [track['id'] for track in random_track]
    x = ['spotify:track:' + y for y in track_ids]
    print(x)

    # add rnd of rnd to lib
    was_added_to_library = spotify_client.add_tracks_to_playlist(track_ids=x, playlist_id=playlist_id
                                                                 , ADD_TO_PLAYLIST_TOKEN=ADD_TO_PLAYLIST_TOKEN)
    if was_added_to_library:
        for track in random_track:
            print(f"Added{track['name']} to your library")


if __name__ == '__main__':
    run()
