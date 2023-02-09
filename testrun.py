import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import cv2
from deepface import DeepFace
import json
import webbrowser
import random
import pandas as pd


def face():
    vid = cv2.VideoCapture(0)
    while(True):
        
        ret, frame = vid.read()
        break


    result = DeepFace.analyze(frame,actions=['emotion'])

    dom_emo=result[0]['dominant_emotion']
    print(dom_emo)

    vid.release()
    cv2.destroyAllWindows()
    a = dom_emo

def spotify(a):
    if (a == 'happy'):
        df = pd.read_csv(
            'C:/Users/CHAITANYA/OneDrive/Desktop/Internet Programming/src/css/songs_normalize.csv')
    elif (a == 'sad'):
        df = pd.read_csv(
            'C:/Users/CHAITANYA/OneDrive/Desktop/Internet Programming/src/css/songs_normalize.csv')
    elif (a == 'surprise'):
        df = pd.read_csv(
            'C:/Users/CHAITANYA/OneDrive/Desktop/Internet Programming/src/css/songs_normalize.csv')
    elif (a == 'fear'):
        df = pd.read_csv(
            'C:/Users/CHAITANYA/OneDrive/Desktop/Internet Programming/src/css/songs_normalize.csv')
    elif (a == 'angry'):
        df = pd.read_csv(
            'C:/Users/CHAITANYA/OneDrive/Desktop/Internet Programming/src/css/songs_normalize.csv')
    elif (a == 'disgust'):
        df = pd.read_csv(
            'C:/Users/CHAITANYA/OneDrive/Desktop/Internet Programming/src/css/songs_normalize.csv')
    elif (a == 'neutral'):
        df = pd.read_csv(
            'C:/Users/CHAITANYA/OneDrive/Desktop/Internet Programming/src/css/songs_normalize.csv')
        
    sname = df.song
    nrow = len(sname.axes[0])

    ran = random.randint(0, nrow)

    print(ran)

    username = 'mvmd286d8k1lyj6ohpi5w7ypv'
    clientID = 'd80df6e1f61246349529e343ed2ec808'
    clientSecret = 'd850f9f6dbe94b36bf2807a87b932972'
    redirect_uri = 'http://google.com/callback/'

    oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
    token_dict = oauth_object.get_access_token()
    token = token_dict['access_token']
    spotifyObject = spotipy.Spotify(auth=token)
    user_name = spotifyObject.current_user()

    print(json.dumps(user_name, sort_keys=True, indent=4))

    while True:
        search_song = sname[ran]
        results = spotifyObject.search(search_song, 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        webbrowser.open(song)
        print('Song has opened in your browser.')
        break



face()
spotify(a)