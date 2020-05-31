from requests import get, post;
from flask import request, redirect, jsonify, Flask;
from json import loads, load
from auth import app_auth, auth_token
from spotify_data import profile_data, create_playlist, search_track, add_track, create_uri;

with open('tracks.json') as file:
    songlist = load(file)

app = Flask(__name__)

@app.route('/')
def login():
    authourization_url = app_auth();
    return redirect(authourization_url);

@app.route('/callback')
def callback():
    code = request.args['code']
    token_dict = loads(auth_token(code))
    access_token = token_dict['access_token']
    refresh_token = token_dict['refresh_token']
    print(access_token)
    profile = profile_data(access_token)
    profile_url = profile['href']

    playlist_desc = "List of Top 40 songs from 2002 - 2011";
    playlist_title = "Top Songs 2000s"; category = "Pop";

    new_playlist = create_playlist(access_token, profile_url, playlist_title, playlist_desc);
    playlist_id = new_playlist['id']

    for song in songlist:
        notadded = []
        track = search_track(access_token, song["song"], song["artist"], 2)
        if track != 0:
            response = add_track(access_token, playlist_id, track);
        else:
            notadded.append()
    
    # Uncomment the line below and comment the for loop if your sonlist is 100 and less
    ''' response = add_track(access_token, playlist_id, uris_list) '''
    return response;


app.run(port=8080, debug=True)