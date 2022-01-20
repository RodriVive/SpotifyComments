from types import NoneType
import spotipy
import spotipy.util as util
from dotenv import dotenv_values


def main(username):
    # Access secret values
    env = dotenv_values('.env')
    # Get a token to acces user info
    scope = 'user-read-currently-playing user-read-recently-played user-read-playback-state'
    token = util.prompt_for_user_token(username, scope, client_id=env['client_id'], client_secret=env['client_secret'], redirect_uri='http://127.0.0.1:9090')
    currentSong(token, username)

def currentSong(token, username):
    if token:
        # Creates new spotify object with the given token to access user info
        sp = spotipy.Spotify(auth=token)
        # Get username
        user = sp.current_user()
        print(user['id'])
        # Check if spotify is currently running
        test = sp.current_playback()
        
        # If spotify is currently not running
        if isinstance(test, NoneType):
            # Get last played song
            lastPlayed = sp.current_user_recently_played(1)
            print(lastPlayed['items'][0]['track']['name'], lastPlayed['items'][0]['track']['uri'])
            # Check to see when spotify is started
            while isinstance(test, NoneType):
                test = sp.current_playback()
            
        # Once spotify runs check current song
        song = sp.current_user_playing_track()
        print(song['is_playing'])
        print(song['item']['name'], song['item']['uri'])
        
        # Check if current song changes
        while(True):
            check = sp.current_user_playing_track()
            if song['item']['name'] != check['item']['name']:
                song = check
                print(song['item']['name'], song['item']['uri'])
            
env = dotenv_values('.env')      
main(env['username'])

