import io
from google.cloud import speech

client= speech.SpeechClient()

audio_file= io.open("output.wav", 'rb')

content= audio_file.read()

audio= speech.RecognitionAudio(content=content)

config= speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=24000,
    language_code="en-US",
)

response= client.recognize(config=config, audio=audio)
print(response)