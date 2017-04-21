import unittest
from youtubeplug.py import *

class TestYoutubePlug(unittest.TestCase):

    def test_audio_equals_hello(self):
        r = sr.Recognizer()
        with sr.AudioFile("Hello.m4a") as source:
            print("What do you want to search for?")
            audio = r.listen(source)
            result = r.recognize_google(audio)
            self.assertEqual(result.lower(), 'hello')


    def test_YoutubeSearch(self):
        result = YouTubeSearch("somewhere over the rainbow")
        self.assertEqual(result, "https://www.youtube.com/watch?v=V1bFr2SWP1I")


    def test_voiceRecognition(self):
        result = voiceRecognition("HelloWorld.m4a")
        self.self.assertEqual(result.lower(), "hello world")


if __name__ == '__main__':
    unittest.main()
