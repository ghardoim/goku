import pyperclip as clip
import teclado as tecla
import time as time
import re as regex

def acha_sorteio(publicacao):
  tecla.tab(2 + publicacao, "")
  tecla.enter(tempo = 3)
  tecla.tab(2, "shift")


def marca(sorteio):

  for a in range(0, (sorteio.amigos * sorteio.comentarios) - 1, sorteio.amigos):

    if 1 == sorteio.amigos:
      tecla.escreve(tempo = 5, texto = f"@{sorteio.marcar[a]}")

    elif 2 == sorteio.amigos:
      tecla.escreve(tempo = 5, texto = f"@{sorteio.marcar[a]} @{sorteio.marcar[a + 1]}")
    
    elif 3 == sorteio.amigos:
      tecla.escreve(tempo = 5, texto = f"@{sorteio.marcar[a]} @{sorteio.marcar[a + 1]} @{sorteio.marcar[a + 2]}")
    
    tecla.tab(1, "")
    tecla.enter(tempo = 1)
    time.sleep(20)
    tecla.tab(2, "shift")

def get_amigos(quantos):
  tecla.tab(3, "")
  tecla.end()
  time.sleep(1)
  for amigo in range(quantos):
    tecla.tab(3, "")
    tecla.botao_direito(tempo = 1)
    tecla.down(vezes = 4)
    tecla.enter(tempo = 1)
    print(regex.search("https://www.instagram.com/(.*)/", clip.paste()).group(1))
