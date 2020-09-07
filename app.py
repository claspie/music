from flask import request, redirect, Flask
from json import loads
from auth import app_auth, auth_token
from spotify_data import profile_data, create_playlist, search_track, add_track, create_urilist, add_to_playlist
from db import fetch

app = Flask(__name__)

songs = fetch()


@app.route('/')
def login():
    authourization_url = app_auth()
    return redirect(authourization_url)


@app.route('/callback')
def callback():
    code = request.args['code']
    token_dict = loads(auth_token(code))
    access_token = token_dict['access_token']
    refresh_token = token_dict['refresh_token']
    print(access_token)
    profile = profile_data(access_token)
    profile_url = profile['href']

    playlist_desc = "List of pop songs from 2002 to 2004"
    playlist_title = "2000s Pop"
    category = "Pop"

    new_playlist = create_playlist(access_token, profile_url, playlist_title, playlist_desc)
    playlist_id = new_playlist['id']
    print(playlist_id)
    urilist = create_urilist(access_token, songs, 2)

    try:
        for song in songs:
            add_to_playlist(access_token, song["name"], song["artist"], 2, playlist_id)
            return "Done"
    except Exception as error:
        print(error)


if __name__ == "__main__":
    app.run(port=8080, debug=True)
