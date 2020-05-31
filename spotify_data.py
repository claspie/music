from requests import get, post;
import keys.keys as key;
from json import loads, dumps
from db import fetch, insert;

CLIENT_ID = key.CLIENT_ID;
CLIENT_SECRET = key.CLIENT_SECRET;

# Spotify URLs
AUTH_URL = "https://accounts.spotify.com/authorize"
TOKEN_URL = "https://accounts.spotify.com/api/token"
API_BASE_URL = "https://api.spotify.com"
API_VERSION = "v1"
API_URL = f"{API_BASE_URL}/{API_VERSION}"


def profile_data(token):
    user_profile_endpoint = f"{API_URL}/me"
    headers = {
    'Authorization': f"Bearer {token}",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.spotify.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
    response = get(user_profile_endpoint, headers=headers)
    data = loads(response.text)
    return data;

def create_playlist(token, user, name, desc):
    url = f"{user}/playlists"
    deets = {
        "name": name,
        "description": desc
    }
    payload = dumps(deets)
    headers = {
    'Content-Type': "application/json",
    'Authorization': f"Bearer {token}",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.spotify.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
    create = post(url, data=payload, headers=headers)
    data = loads(create.text)
    return data;

def search_track(token, name, artist, number):
    url = f"{API_URL}/search"
    artist_name = artist.lower();
    querystring = {
        "q": f"{name} artist:{artist_name}",
        "type": "track",
        "limit": number
    }
    payload = ""
    headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Authorization': f"Bearer {token}",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.spotify.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
    search = get(url, data = payload, headers=headers, params=querystring)
    data = loads(search.text)
    if len(data['tracks']['items']) != 0:
        track_uri = data['tracks']['items'][0]['uri']
        return track_uri
    else:
        return 0;

def add_tracks(token, playlist_id, songs):
    url = f"{API_URL}/playlists/{playlist_id}/tracks"
    payload = dumps(songs)
    headers = {
    'Content-Type': "application/json",
    'Authorization': f"Bearer {token}",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.spotify.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
    add_song = post(url, data=payload, headers=headers)
    return loads(add_song.text);

def add_track(token, playlist_id, song):
    url = f"{API_URL}/playlists/{playlist_id}/tracks"
    querystring = {"uris": str(song)}
    payload = ""
    headers = {
    'Content-Type': "application/json",
    'Authorization': f"Bearer {token}",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "api.spotify.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }
    add_song = post(url, data=payload, headers=headers, params=querystring)
    return loads(add_song.text);

def create_urilist(token, songlist, number):
    uris = []

    for song in songlist:
        song_uri = search_track(token, song['name'], song['artist'], number);
        if song_uri == 0 or song_uri == "":
            pass;
        else:
            uris.append(song_uri);

    return uris;


def add_to_playlist(token, song_name, artist, limit_number, playlist_id):
    track_uri = search_track(token, song_name, artist, limit_number);
    if type(track_uri) is int:
        nsong = {
            "song": song_name,
            "artist": artist
        }
        with open('not_found.json', 'a') as file:
            file.write(nsong, "\n")
        
    else:
        add_song_playlist = add_track(token, playlist_id, track_uri)
        print("song added to pl")
    

if __name__ == "__main__":
    songs =fetch()
    playlist = "2XVt7LQBD6qxRi3OS5a82M"
    token = "BQCR0B48_YT4h8hwi_iSFPH_qnaOo2gGMyhtOG-NcXXxLeVu1Ut8aPNy6Jp7d-OWeZ3U8VtNG6bafBgTuWZ1xDnUDEgy0wQcUvMoTR4aqksKm8DGSc7CIExRKdtGCAN_LwXPcgRLwoLq09yMqhNE-gWUFlbOvp1N9z6ZRqd6N2QOnljMQPnny4o03nOTdvdMdNVKLwwsG4OuarHM8W8_7dNmX8eFb_AQQKNwtkQ"
    for song in songs:
        add_to_playlist(token, song["name"], song["artist"], 2, playlist)
        
        print("song added")