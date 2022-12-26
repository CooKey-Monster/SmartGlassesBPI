import threading
from google.cloud import speech
from google.oauth2 import service_account
from valuePrinter import listen_print_loop

class SpeechAPI:
    def __init__(self, creds, RATE, CHUNK, language_code):
        self.RATE = RATE
        self.CHUNK = CHUNK

        self.language_code = language_code

        self.configure()
        
        # Loading credentials
        self.credentials = service_account.Credentials.from_service_account_file(
                creds)

        self.scoped_credentials = self.credentials.with_scopes(
                ['https://www.googleapis.com/auth/cloud-platform'])
    
    def authenticate(self):
        return speech.SpeechClient(credentials=self.credentials)

    def configure(self):
        #"en-CA"  # a BCP-47 language tag

        # Recognition settings  
        self.config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=self.RATE,
            language_code=self.language_code,
        )

        self.streaming_config = speech.StreamingRecognitionConfig(
            config=self.config, interim_results=True
        )

    def recognize(self, MicrophoneStream, ui, auth):
        # Recognizing cycle
        with MicrophoneStream(self.RATE, self.CHUNK) as stream:
            # Generate audio
            self.audio_generator = stream.generator()

            print("Listening")
            
            # Send request to recognize speech
            self.requests = (
                speech.StreamingRecognizeRequest(audio_content=content)
                for content in self.audio_generator
            )

            # Recognize speech
            self.responses = auth.streaming_recognize(self.streaming_config, self.requests)

            # Print result
            threading.Thread(target=ui.main).start()
            self.gen = listen_print_loop(self.responses)
            for response in self.gen:
                print(response)
                ui.update_text(response)