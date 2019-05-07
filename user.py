import oauth
import linkedlist
import songInfo
import json
import spotipy

#class for the users of the program


class User(object):
    def __init__(self, username=None):
        self.sp = oauth.create_new_spotipy(username)
        #spotipy object for user
        self.list = linkedlist.linkedlist()
        #list for user data

    def get_most_recent_songs(self):
        results=self.sp.current_user_recently_played(limit=50)
        for i, track in enumerate(results['items']):
            id = track['track']['id']
            timestamp = track['played_at']
            name = track['track']['name']
            song = songInfo.songInfo(id=id,timestamp=timestamp,name=name)
            self.list.add(data=song)
            print(song.get_name())


kolbe = User(username='shockedeel')
kolbe.get_most_recent_songs()
kolbe.list.print()





