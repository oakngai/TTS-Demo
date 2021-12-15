import os, io
from google.cloud import texttospeech_v1
from google.cloud.texttospeech_v1.types.cloud_tts import SsmlVoiceGender
import ocr_from_image
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\User\worktest\envtest\propane-ripsaw-333014-fc7e99359aa9.json"

client = texttospeech_v1.TextToSpeechClient()

text1 = str(ocr_from_image.df1['description1'][0])
text2 = str(ocr_from_image.df2['description2'][0])

synthesis_input1 = texttospeech_v1.SynthesisInput(text=text1)
synthesis_input2 = texttospeech_v1.SynthesisInput(text=text2)

#1
voice1 = texttospeech_v1.VoiceSelectionParams(
    name='th-TH-Standard-A',
    language_code='th-TH'   
)

#2
voice2 = texttospeech_v1.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech_v1.SsmlVoiceGender.MALE
)

#Output file config
audio_config = texttospeech_v1.AudioConfig(
    audio_encoding=texttospeech_v1.AudioEncoding.MP3
)


response1 = client.synthesize_speech(
    input=synthesis_input1,
    voice=voice1,
    audio_config=audio_config
)

response2 = client.synthesize_speech(
    input=synthesis_input2,
    voice=voice2,
    audio_config=audio_config
)

with open('audio_file1.mp3', 'wb') as output1:
    output1.write(response1.audio_content)

with open('audio_file2.mp3', 'wb') as output1:
    output1.write(response2.audio_content)
