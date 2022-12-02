from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

# Recognize
from google.cloud import speech_v1 as speech

# Authenticate
from google.oauth2 import service_account

# Convert
from os.path import splitext
from pydub import AudioSegment

class Recognizer:
    def __init__(self, audio_file):
        self.audio_file = audio_file

        self.credentials = service_account.Credentials.from_service_account_file(
            'passwords/key.json')

        self.scoped_credentials = self.credentials.with_scopes(
            ['https://www.googleapis.com/auth/cloud-platform'])

        self.config = speech.RecognitionConfig(
            sample_rate_hertz=44100,
            enable_automatic_punctuation=True,
            language_code='en-US'
        )

        self.flac_location = "idk2.flac"
        #self.load()
        self.flac_file = dict(uri="gs://bigmonkeys/idk2.flac")

    def load(self):
       self.flac_path = "%s.flac" % splitext(self.audio_file)[0]
       self.song = AudioSegment.from_mp3(self.audio_file)
       self.song.export(self.flac_location, format = "flac") 

    def speech_to_text(self):
        self.client = speech.SpeechClient(credentials=self.credentials)
        self.response = self.client.recognize(config=self.config, audio=self.flac_file)
        self.print_sentences(self.response)

    def print_sentences(self, response):
        for result in response.results:
            self.best_alternative = result.alternatives[0]
            self.transcript = self.best_alternative.transcript
            self.confidence = self.best_alternative.confidence
            print("-" * 80)
            print(f"Transcript: {self.transcript}")
            print(f"Confidence: {self.confidence:.0%}")

if __name__ == '__main__':
    # Authenticate
    audio = "idk.mp3"
    api = Recognizer(audio)
    
    # Recognize 
    api.speech_to_text()
