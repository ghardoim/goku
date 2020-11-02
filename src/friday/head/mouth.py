from playsound import playsound as play
from gtts import gTTS as gravar
import os as system

music_file = 'resource/music/goku.mp3'

def fala(fala):
  
  speech = gravar(text = fala, lang = 'pt')
  speech.save(music_file)

  play(music_file)

  system.remove(music_file)