import voiceRecognition;
import YouTube API;
import Django;
from tkinter import *;

# Will return a string from user spoken words recorded
# by the microphone in computer or mobile device
def voiceRecognition():
    return

# Take the value from voiceRecognition() run a search
# in YouTube and yield a video using predefined functions
def YouTubeSearch(string):
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
