from requests import get, post
import keyring
from json import loads, dumps

CLIENT_ID = keyring.get_password('spotify', 'id')
CLIENT_SECRET = keyring.get_password('spotify', 'password')

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
    return loads(response.text)


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
    return loads(create.text)


def search_track(token, name, artist, number):
    url = f"{API_URL}/search"
    artist_name = artist.lower()
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
    search = get(url, data=payload, headers=headers, params=querystring)
    data = loads(search.text)
    if len(data['tracks']['items']) != 0:
        return data['tracks']['items'][0]['uri']
    else:
        return 0


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
    return loads(add_song.text)


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
    return loads(add_song.text)


def create_urilist(token, songlist, number):
    uris = []

    for song in songlist:
        song_uri = search_track(token, song['name'], song['artist'], number)
        if song_uri not in [0, ""]:
            uris.append(song_uri)

    return uris


def add_to_playlist(token, song_name, artist, limit_number, playlist_id):
    track_uri = search_track(token, song_name, artist, limit_number)
    if type(track_uri) is int:
        nsong = {
            "song": song_name,
            "artist": artist
        }
        with open('not_found.json', 'a') as file:
            file.write(dumps(nsong))

    else:
        add_track(token, playlist_id, track_uri)
        print("song added to pl")


if __name__ == "__main__":
    pass
