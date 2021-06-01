from google.cloud import texttospeech

client= texttospeech.TextToSpeechClient()

input_text= texttospeech.SynthesisInput(text="Hi! KyungwoonUniversity!")

voice= texttospeech.VoiceSelectionParams(
    language_code="en-US",
    name="en-US-Standard-C",
    ssml_gender=texttospeech.SsmlVoiceGender.FEMALE,
)

audio_config= texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16
)

response= client.synthesize_speech(
    request={"input": input_text, "voice": voice, "audio_config": audio_config}
)

with open("output.wav", "wb") as out:
    out.write(response.audio_content)
    print('Audiocontentwrittentofile"output.mp3"')