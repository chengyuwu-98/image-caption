import pyttsx3
from google.cloud import texttospeech


def read_text(text):
    engine = pyttsx3.init()  # object creation

    """ RATE"""
    engine.setProperty('rate', 125)     # setting up new voice rate

    """VOLUME"""
    engine.setProperty('volume', 1.0)    # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')       # getting details of current voice
    engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 1 for female

    engine.say(text)
    engine.runAndWait()
    engine.stop()

def text2speech(text):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()

    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    return response.audio_content