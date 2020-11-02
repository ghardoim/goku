import speech_recognition as sr

def ouve():

  rec = sr.Recognizer()
  with sr.Microphone() as microfone:
    rec.adjust_for_ambient_noise(microfone)
    audio = rec.listen(microfone)

    return rec.recognize_google(audio, language = "pt-BR")