import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests
from pprint import pprint

SPOTIFY_CLIENT_ID = YOUR_CLIENT_ID
SPOTIFY_CLIENT_SECRET = YOUR_CLIENT_SECRET
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

URL="https://www.billboard.com/charts/hot-100"
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(f"{URL}/{date}")
soup = BeautifulSoup(response.text, "html.parser")
songs_tag = soup.findAll(name="span", class_="chart-element__information__song")
songs = [song.getText() for song in songs_tag]

song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{songs[0]} year:{year}", type="track")

    try:
        uri = result['tracks']['items'][0]['uri']
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)