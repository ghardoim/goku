import pyperclip as clip
import teclado as tecla
import time as time
import re as regex

def acha_sorteio(publicacao):
  tecla.tab(vezes = 2 + publicacao)
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
    
    tecla.tab(vezes = 1)
    tecla.enter(tempo = 1)
    time.sleep(20)
    tecla.tab(
      2, "shift")

def carrega_amigos():
  tecla.tab(vezes = 2)
  tecla.end(tempo = 1, vezes = 1)
  tecla.tab(vezes = 2)
  tecla.end(tempo = 1, vezes = 10)
  tecla.esc(tempo = 1)

def get_amigos(quantos):
  nomes = []
  time.sleep(2)
  for amigo in range(quantos):
    tecla.tab(vezes = 3)
    tecla.botao_direito()
    time.sleep(2)
    tecla.seta(vezes = 4, seta = "down")
    tecla.enter(tempo = 2)
    nome = regex.search("com/(.*)/", clip.paste()).group(1)
    nomes.append(nome)
  print(nomes)
  return nomes

def quantos_sigo():
  tecla.botao_direito()
  tecla.esc(tempo = 2)
  tecla.botao_direito()
  tecla.seta(vezes = 1, seta = "up")
  tecla.enter(tempo = 1)
  time.sleep(5)
  tecla.seta(vezes = 2, seta = "right")
  tecla.ctrl("c")
  copy = clip.paste()
  time.sleep(1)
  tecla.ctrl("i", "shift")
  string = regex.search(">(.*)<", copy).group(1)
  return int(string)