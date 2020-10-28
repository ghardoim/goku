from src.friday.head.voice import Ouve, Fala
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
  
  texto = Ouve()
  Fala(texto)
