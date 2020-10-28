from playsound import playsound as play
import speech_recognition as sr
from gtts import gTTS as gravar
import os as system
import time as time

music_file = 'resource/music/goku.mp3'

def Ouve():

  rec = sr.Recognizer()
  with sr.Microphone() as microfone:
    rec.adjust_for_ambient_noise(microfone)

    print("estou ouvindo")
    audio = rec.listen(microfone)
    return rec.recognize_google(audio, language = "pt-BR")

def Fala(fala):
  
  print(f"{fala}")
  speech = gravar(text = fala, lang = 'pt')
  speech.save(music_file)
  play(music_file)

def delete_file():

  time.sleep(2)
  system.remove(music_file)