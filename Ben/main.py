from ProjectUI import SpeechUI
from speechAPI import SpeechAPI
from microphoneStream import RATE, CHUNK
from microphoneStream import MicrophoneStream

if __name__ == '__main__':
    # Initializing the UI for the project
    ui = SpeechUI()

    # See http://g.co/cloud/speech/docs/languages
    # for a list of supported languages.
    language_code = "en-CA"  # a BCP-47 language tag

    # Authenticate and recognize
    client = SpeechAPI("../passwords/key.json", RATE, CHUNK, language_code)
    auth = client.authenticate()
    client.recognize(MicrophoneStream, ui, auth)