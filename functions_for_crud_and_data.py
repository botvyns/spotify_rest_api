import logging
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='###',
                                               client_secret='###',
                                               redirect_uri='###',
                                               scope='playlist-read-private playlist-modify-public playlist-modify-private'))

# configuring the logging to write to a file
logging.basicConfig(filename='app_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

def get_input_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            input_data = json.load(file)
            return input_data
    except Exception as e:
        logging.error(f"Error reading input file: {e}")
        return None

def add_tracks_to_playlist(playlist_id, track_uris):
    try:
        sp.playlist_add_items(playlist_id, track_uris)
        logging.info(f"Tracks added successfully to playlist {playlist_id}")
    except Exception as e:
        logging.error(f"Error adding tracks to playlist {playlist_id}: {e}")

def get_playlist_details(playlist_id):
    try:
        playlist = sp.playlist(playlist_id)
        logging.info(f"Playlist details retrieved successfully for playlist {playlist_id}")
        return playlist
    except Exception as e:
        logging.error(f"Error getting playlist details for {playlist_id}: {e}")
        return None

def update_playlist_details(playlist_id, new_name):
    try:
        sp.playlist_change_details(playlist_id, name=new_name)
        logging.info(f"Playlist details updated successfully for playlist {playlist_id}")
    except Exception as e:
        logging.error(f"Error updating playlist details for {playlist_id}: {e}")

def remove_tracks_from_playlist(playlist_id, track_uris):
    try:
        sp.playlist_remove_all_occurrences_of_items(playlist_id, track_uris)
        logging.info(f"Tracks removed successfully from playlist {playlist_id}")
    except Exception as e:
        logging.error(f"Error removing tracks from playlist {playlist_id}: {e}")