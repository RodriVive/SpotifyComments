from __future__ import print_function
from sys import platlibdir
import spotipy
import spotipy.util as util
from dotenv import dotenv_values


def main(username):
    env = dotenv_values('secrets.env')
    scope = 'user-read-currently-playing user-read-recently-played'
    token = util.prompt_for_user_token(username, scope, client_id=env['client_id'], client_secret=env['client_secret'], redirect_uri='http://127.0.0.1:9090')
    currentSong(token, username)

def currentSong(token, username):
    if token:
        sp = spotipy.Spotify(auth=token)
        user = sp.current_user()
        print(user['id'])

        song = sp.current_user_playing_track()
        print(song['is_playing'])
        
        if song['is_playing'] == False:
            lastPlayed = sp.current_user_recently_played(1)
            print(lastPlayed['items'][0]['track']['name'], lastPlayed['items'][0]['track']['uri'])

        while(True):
            check = sp.current_user_playing_track()
            if song['item']['name'] != check['item']['name']:
                song = check
                print(song['item']['name'], song['item']['uri'])
            
            
main('rodrigo.villegas.')

