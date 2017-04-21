import speech_recognition as sr
import webbrowser
import time
from gtts import gTTS
import os
#import YouTubeAPI
#import Django
#from apiclient.discovery import build
#from apiclient.errors import HttpError
#from oauth2client.tools import argparser
from tkinter import *

DEV_API_KEY = "AIzaSyADIqaClVv1ibPuIx7v2Gq4eNlfhHu1T30"


def voiceRecognition(audioFile):
# for testing purposes
# Will return a string from user spoken words recorded
# by the microphone in computer or mobile device

    # Text to Speech
    tts = gTTS(text='What do you want to search for?', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")
    r = sr.Recognizer()
    with sr.AudioFile(audioFile) as source:
        print("What do you want to search for?")
        audio = r.listen(source)

    # https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
    # recognize speech using Google Speech Recognition
    try:
        searchText = r.recognize_google(audio)
        print("I heard '" + searchText + "'")
    except sr.UnknownValueError:
        print("We could not understand you, please try again")
    except sr.RequestError as e:
        print("Error: ; {0}".format(e))

    # Confirm search with text to speech
    tts = gTTS(text="Did you mean to say '" + searchText + "'?'", lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

    with sr.AudioFile(audioFile) as source:
        print("Did you mean to say '" + searchText + "'?")
        audio2 = r.listen(source)
    listenedTwo = "yes"

    # Check confirmation voice cue
    if ('yes' == listenedTwo):
        tts = gTTS(text="Ok, searching for'" + searchText + "'?'", lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
        print("OK, searching for '" + searchText + "'")
        YouTubeSearch(searchText)
        return searchText
    else:
        print("OK, not searching")
        return searchText


def voiceRecognition():
# Will return a string from user spoken words recorded
# by the microphone in computer or mobile device

    # Text to Speech
    tts = gTTS(text='What do you want to search for?', lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What do you want to search for?")
        audio = r.listen(source)

    # https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
    # recognize speech using Google Speech Recognition
    try:
        searchText = r.recognize_google(audio)
        print("I heard '" + searchText + "'")
    except sr.UnknownValueError:
        print("We could not understand you, please try again")
    except sr.RequestError as e:
        print("Error: ; {0}".format(e))

    # Confirm search with text to speech
    tts = gTTS(text="Did you mean to say '" + searchText + "'?'", lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

    with sr.Microphone() as source:
        print("Did you mean to say '" + searchText + "'?")
        audio2 = r.listen(source)
    listenedTwo = r.recognize_google(audio2)

    # Check confirmation voice cue
    if ('yes' == listenedTwo):
        tts = gTTS(text="Ok, searching for'" + searchText + "'?'", lang='en')
        tts.save("good.mp3")
        os.system("mpg321 good.mp3")
        print("OK, searching for '" + searchText + "'")
        YouTubeSearch(searchText)
        return searchText
    else:
        print("OK, not searching")
        return searchText

def YouTubeSearch(inputStr):
    # Take the value from voiceRecognition() run a search
    # in YouTube and yield a video using predefined functions

    yt = build("youtube", "v3", developerKey= DEV_API_KEY)

    search_results = yt.search().list(q = inputStr, part = "id, snippet", maxResults = 1).execute()

    videos = []

    for search_result in search_results.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
          videos.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["videoId"]))
          print("Opening: https://www.youtube.com/watch?v=" + search_result["id"]["videoId"])
          webbrowser.open("https://www.youtube.com/watch?v=" + search_result["id"]["videoId"])
          return "https://www.youtube.com/watch?v=" + search_result["id"]["videoId"]
    # print out list of videos
    # print(videos)

    # search_result = search_results[0]
    # vidID = search_result["id"]["videoId"]
    # print("https://www.youtube.com/watch?v=" + "vidID")


def UI():
    # basic UI to give an idea of what the application should look like
    # in a letter version will probably change it to a better UI using another
    # imported library

    base = Tk()
    base.title("Youtube Plugin")
    base.geometry("255x200")
    frame = Frame(base)
    frame.pack()

    promptVoiceRecognition = Button(frame, text = 'Prompt Voice Recognition', fg='Black', command = voiceRecognition)
    promptVoiceRecognition.pack(side = TOP)

    saveToPlaylist = Button(frame, text = 'Save To Playlist', fg='Black')
    saveToPlaylist.pack(side = TOP)

    base.mainloop()

def main():
    YouTubeSearch("over the rainbow")

main()
