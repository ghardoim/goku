from src.friday.voice.musica import Ouve, Fala, delete_file
import src.friday.hands.mouse as mouse
from src.model.sorteio import Sorteio
from src.view.app import Application

sorteio = Sorteio("resource/json/sorteio.json")
browser = "edge"
mouse.vai_pro_canto()

import pyttsx3 

if __name__ == "__main__":
  # goku = Application(sorteio, browser)
  # goku.mainloop()
  Fala("Diz pra mim!")
  delete_file()
  texto = Ouve()
  Fala(texto)
  delete_file()
