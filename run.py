import os
from spotify_client import SpotifyClient

Create_Playlist_TOKEN = "BQB_0C4_YKgBxl2-qMyoBJfU7SUE1gPiS8j3HWHr28BvHRAZ3Y_9xEFZhiXgc65LbgDSvkyqeVMif4Ni_FQ4Gy0bzBX13fqbs2L2fqzol-lRDVi2pG_SBn7Y4f0v_sYK1h16a9h2K_xGZYzCNf8issND1Jg_xP34mYyAvDavJMnUQDT0o-nOv8FOA9H62p-i5vJvVvuIgF3Q9nqJUMqJ8fIFcO87drnaJ1hbR6aCNuVH"
PlaylistName = "RandomPlaylist"
ADD_TO_PLAYLIST_TOKEN = "BQCPMHycFLjdw1URVSm1iakKWz7XTmO5iTDQ32zqVddx7OuIBjXkkY4ixHRCTPYqyb3nNFufsypPxzpxhwNyKmyUvSg7_mF0685WDty6j49GmdgYo-UNgrq4eYKLyHwEf2DZ492kOdpR5vSFazk8pn2hVcF_U4dPKkpcXkYKm294HaSrLOVoJ6xj0AwaxITyn5p4TVZS-z9xSOtf_8yooAAzY-zyxCcJVIdMBycinyYY"
TOKEN = "BQD5QPRzI3YBlzXUAvixrc3dC6h93vFyz8JJrcmZ1Er6TQZ6yECSF0YUqNrZWcM9ooiXaH5B5-ws38z-5VZurbxwgplk3LjvNLmt_g8Qh2XujUJG_A-0zgU-o2c-FrBW-i-N79fImGAEJsy2xMC-Mg5s7_JGVO83rKinZ-aMLYMmvstHt92rN7v1ROWv"


def run():
    # search for rnd songs
    spotify_client = SpotifyClient(os.getenv('SPOTIFY_AUTH_TOKEN'))
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
