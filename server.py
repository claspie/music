from flask import Flask, jsonify, redirect, request
from auth import app_auth, user_auth, Profile_Data, Search_Track, Add_Playlist, Add_Track, Playlist_Data
import mysql.connector, keys.dbm as dbm, data

mydb = mysql.connector.connect(
    host = dbm.host,
    user = dbm.user,
    passwd = dbm.password,
    database = dbm.db
)

app = Flask(__name__)

@app.route("/")
def index():
    # Authorization
    auth = app_auth()
    return redirect(auth)

@app.route("/callback")
def callback():
    authorization_header = user_auth()
    
    profile = Profile_Data(authorization_header)
    
    new_playlist = Add_Playlist(authorization_header, profile, "Songs from 2005", "Some of the best from 2005 to 2018")
    print("Successfully created Playlist")
    
    playlist_songs = data.Fetch_Songs()
    
    for song, artist in playlist_songs:
        songs_list = []
        response = Search_Track(authorization_header,song)
        for i in range(0,3):
            uri = response['tracks']['items'][i]['uri']
            songs_list.append(uri)
            i += 1
        Add_Track(authorization_header, profile, new_playlist, songs_list)
    return "Playlist Creation has ended without errors"

if __name__ == "__main__":
    app.run(debug=True, port=8080)
