from sorteio import Sorteio
from app import Application
import mouse as mouse

sorteio = Sorteio("sorteio.json")
browser = "edge"
mouse.vai_pro_canto()

if __name__ == "__main__":
  goku = Application(sorteio, browser)
  goku.mainloop()