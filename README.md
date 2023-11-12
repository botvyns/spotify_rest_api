# spotify_rest_api
A tiny project to get aquainted with REST API (spicifically Spotify REST API)

File [functions_for_crud_and_data.py](https://github.com/botvyns/spotify_rest_api/blob/main/functions_for_crud_and_data.py) contains functions that will read data in json file, add new tracks to the playlist, get the playlist details, change the playlist name and delete specified songs. The last four represent CRUD operations. Any information like sucessful operation execution, errors will be logged into file app_log.txt

File [perform_crud.py](https://github.com/botvyns/spotify_rest_api/blob/main/perform_crud.py) imports and executes specified functions.

File [input_data.json](https://github.com/botvyns/spotify_rest_api/blob/main/input_data.json) is an example of how your data might look like. To put yours, you will have to specify URIs for playlist, tracks and preferable list name. 
