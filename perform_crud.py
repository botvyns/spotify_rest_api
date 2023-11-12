from functions_for_crud_and_data import get_input_from_file, get_playlist_details, add_tracks_to_playlist, update_playlist_details, remove_tracks_from_playlist

file_path = 'input_data.json'
playlists_data = get_input_from_file(file_path)

if playlists_data:
    for playlist_data in playlists_data:
        playlist_id = playlist_data["playlist_id"]
        track_uris_add = playlist_data["track_uris_add"]
        track_uris_remove = playlist_data["track_uris_remove"]
        new_name = playlist_data["new_name"]

        add_tracks_to_playlist(playlist_id, track_uris_add)

        playlist_details = get_playlist_details(playlist_id)

        update_playlist_details(playlist_id, new_name)

        remove_tracks_from_playlist(playlist_id, track_uris_remove)