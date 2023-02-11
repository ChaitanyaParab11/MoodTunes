import customtkinter as ck
import tkinter as tk
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import cv2
from deepface import DeepFace
import json
import webbrowser
import random
import pandas as pd


def fun1():
    vid = cv2.VideoCapture(0)
    while (True):

        ret, frame = vid.read()

        cv2.imshow('frame', frame)

        if cv2.waitKey(1000):
            break

    result = DeepFace.analyze(frame, actions=['emotion'])

    dom_emo = result[0]['dominant_emotion']
    print(dom_emo)

    vid.release()
    cv2.destroyAllWindows()

    if (dom_emo == 'happy'):
        df = pd.read_csv(
            'assets/happy.csv')
        sname = df.song
    elif (dom_emo == 'sad'):
        df = pd.read_csv(
            'assets/sad.csv')
        sname = df.song
    elif (dom_emo == 'surprise'):
        df = pd.read_csv(
            'assets/surprise.csv')
        sname = df.song
    elif (dom_emo == 'fear'):
        df = pd.read_csv(
            'assets/fear.csv')
        sname = df.song
    elif (dom_emo == 'angry'):
        df = pd.read_csv(
            'assets/angry.csv')
        sname = df.song
    elif (dom_emo == 'disgust'):
        df = pd.read_csv(
            'assets/disgust.csv')
        sname = df.song
    elif (dom_emo == 'neutral'):
        df = pd.read_csv(
            'assets/neutral.csv')
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
    label_3.pack(side="right", fill="both", expand=True)
    label_2 = ck.CTkLabel(frame1, text="Current song: " + sname[ran])
    label_2.pack(side="right", fill="both", expand=True)


ck.set_appearance_mode("system")
ck.set_default_color_theme("blue")


root = ck.CTk()
root.geometry("900x500")
root.title(" MoodTunes ")
# root.iconbitmap("favicon.ico")


frame1 = ck.CTkFrame(root, width=400, height=200)
label1 = ck.CTkLabel(frame1, text=" Code Warriors ")
label1_1 = ck.CTkLabel(frame1, text=" Play Song Based On Your Emotions")
label_3 = ck.CTkLabel(frame1, text=" Changed ")

label1.pack()
label1_1.pack()

Trainbutton = ck.CTkButton(frame1, text="Change Your Song", command=fun1)
Trainbutton.pack()


frame1.pack(side="right", fill="both", expand=True)


root.mainloop()
