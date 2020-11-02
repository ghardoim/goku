from src.friday.head import ear, mouth, brain
# from src.model.sorteio import Sorteio
# from src.view.app import Application
import src.friday.body.moves as atk 
import speech_recognition as voz

# sorteio = Sorteio("resource/json/sorteio.json")
# browser = "edge"
# mouse.vai_pro_canto()

if __name__ == "__main__":
  # goku = Application(sorteio, browser)
  # goku.mainloop()
  
  mouth.fala(brain.hello())
  while True:

    try:
      texto = ear.ouve()
    except Exception:
      mouth.fala("Não ouvi o que você disse!")
    
    else:
      entendi = brain.entenda(texto)
      mouth.fala(entendi["fala"])
      
      if entendi["tipo"] == 1:
        atk.pesquisa_google(texto)
        mouth.fala("Que tal dar uma olhada nisso?")