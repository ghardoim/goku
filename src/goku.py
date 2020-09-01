from sorteio import Sorteio
import instagram as insta
import pyautogui as auto
import teclado as tecla
import time as time

sorteio = Sorteio("resource/sorteio.json")
browser = "edge"

def kamehameha():
  print("Oi, eu sou o Goku!")
  print("Levante as mãos e me ajude a fazer a genki dama enquanto eu faço uns comentários para vc!")
  print(sorteio)
  print("Vou comentar todos esses seus amigos aqui ->")
  for amigo in sorteio.marcar:
    print("\t", amigo)
  print("O meu KI ainda não está bom, mas vou continuar treinando para melhorar isso!!")
  input("Aperte 'enter' e me dê a mão pra fugir desta terrível escuridão")

  tecla.abre_janela(browser)
  tecla.ctrl("l")
  tecla.escreve(tempo = 1, texto = f"instagram.com/{sorteio.pagina}/")
  tecla.enter(tempo = 3)
  tecla.ctrl("f")
  tecla.escreve(1, "publicacoes")
  tecla.enter(tempo = 2)
  tecla.esc()
  tecla.tab(2 + sorteio.publicacao, "")
  tecla.enter(tempo = 3)
  tecla.tab(2, "shift")
  insta.marca(sorteio)
  tecla.tab(1, "")
  tecla.esc()
  tecla.fecha_janela(1)

if __name__ == "__main__":
  kamehameha()