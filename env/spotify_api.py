import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="playlist-read-private"
))

def get_playlist_by_mood(mood):
    genre_map = {
        "positive": "happy",
        "negative": "sad",
        "neutral": "chill"
    }
    genre = genre_map.get(mood, "chill")

    results = sp.search(q=genre, type="playlist", limit=5)
    return [(playlist['name'], playlist['external_urls']['spotify']) for playlist in results['playlists']['items']]

if __name__ == "__main__":
    mood = input("Enter your mood (positive/negative/neutral): ")
    playlists = get_playlist_by_mood(mood)
    for name, link in playlists:
        print(f"{name}: {link}")
