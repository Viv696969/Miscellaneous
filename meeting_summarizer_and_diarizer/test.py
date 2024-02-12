import moviepy.editor as mp
from time import time
import assemblyai as aai
import openai
import json
import os
# from dotenv import load_dotenv

# load_dotenv()


# os.getenv('OPEN_AI_API_KEY')


# openai.api_key = API_KEY_chatgpt
transcriber = aai.Transcriber()
print("transcriber loaded")
st=time()

filename='min_5.mp4'

clip = mp.VideoFileClip(str(filename))
mp3_file_name=filename.split('.')[0]

clip.audio.write_audiofile(f"{mp3_file_name}.mp3")
print("audio file prepared")


config = aai.TranscriptionConfig(speaker_labels=True)

print("config done")
transcript = transcriber.transcribe(f'{mp3_file_name}.mp3', config)



speaker_and_text={}
for utterance in transcript.utterances:
    # print(f"Speaker {utterance.speaker}: {utterance.text}")
    if f"Speaker {utterance.speaker}" in speaker_and_text:
        speaker_and_text[f"Speaker {utterance.speaker}"]=speaker_and_text[f"Speaker {utterance.speaker}"]+"..."+utterance.text
    else:
        speaker_and_text[f"Speaker {utterance.speaker}"]=utterance.text

speaker_text=""
for speaker,sentences in speaker_and_text.items():
    speaker_text=speaker_text+f"{speaker}\n{sentences}\n\n"

    



prompt=f"Summarize the following text in 200 words and dont include words like good morning , hello etc and provide a suitable title .give me the title and sumamry in json format which i can parse for my buisness needs. the text is  {transcript.text}"
output = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content":prompt}]
)

# Print out the whole output dictionary
print(output)
# Get the output text only
# data=json.loads(output['choices'][0]['message']['content'])
# print(data['title'])
# print(data['summary'])
print(speaker_text)
print(transcript.audio_duration)

# aai.settings.api_key = "dedd87116b7544b8b0e2e0c6204c14bb"
# dedd87116b7544b8b0e2e0c6204c14bb
# `pip install openai==0.28

