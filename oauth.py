import spotipy
import sys
import spotipy.util as util
client_id = '9e23b30554fc4bd0afc80be9ec980061'
client_secret = '191e5a4b37234dfc99e7a551820c5485'
scopes = 'user-read-recently-played'
redirect_uri = 'https://google.com/'

def create_new_spotipy(username):
    token=util.prompt_for_user_token(username,scopes,client_id,client_secret,redirect_uri)
    if token:
        sp= spotipy.Spotify(auth=token)
        return sp
    return None

if __name__ == '__main__':
    username = input('username?')
    spotify=create_new_spotipy(username)









