import speech_recognition as sr
import webbrowser;
import pyttsx
#import YouTubeAPI;
#import Django;
#import pyaudio;
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser


from Tkinter import *

DEV_API_KEY = "AIzaSyADIqaClVv1ibPuIx7v2Gq4eNlfhHu1T30"

engine = pyttsx.init()

# Will return a string from user spoken words recorded
# by the microphone in computer or mobile device
def voiceRecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("What do you want to search for?")
        engine.runAndWait()
        audio = r.listen(source)

    #https://github.com/Uberi/speech_recognition/blob/master/examples/microphone_recognition.py
    # recognize speech using Google Speech Recognition
    try:
        searchText = r.recognize_google(audio)
        print("I heard '" + searchText + "'")
    except sr.UnknownValueError:
        print("We could not understand you, please try again")
    except sr.RequestError as e:
        print("Error: ; {0}".format(e))

    #Confirm search
    with sr.Microphone() as source:
        print("Did you mean to say '" + searchText + "'?")
        audio2 = r.listen(source)
    listenedTwo = r.recognize_google(audio2)

    #Check confirmation voice cue
    if ('yes' == listenedTwo):
        print("OK, searching for '" + searchText + "'")
        YouTubeSearch(searchText)
    else:
        print("OK, not searching")


    return

# Take the value from voiceRecognition() run a search
# in YouTube and yield a video using predefined functions
def YouTubeSearch(inputStr):
    yt = build("youtube", "v3", developerKey= DEV_API_KEY)

    search_results = yt.search().list(q = inputStr, part = "id, snippet", maxResults = 1).execute()

    videos = []

    for search_result in search_results.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
          videos.append("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["videoId"]))
          print("Opening: https://www.youtube.com/watch?v=" + search_result["id"]["videoId"])
          webbrowser.open("https://www.youtube.com/watch?v=" + search_result["id"]["videoId"])

    #print out list of videos
    #print(videos)

    #search_result = search_results[0]
    #vidID = search_result["id"]["videoId"]
    #print("https://www.youtube.com/watch?v=" + "vidID")

    return

# basic UI to give an idea of what the application should look like
# in a letter version will probably change it to a better UI using another
# imported library
def UI():
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
    UI()

main()
