import spotipy
import sys
import spotipy.util as util
client_id = ''
client_secret = ''
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









