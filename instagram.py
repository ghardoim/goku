import requests as request
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
      tecla.escreve(tempo = 5, texto = f"@{sorteio.quem_marcar[a]}")

    elif 2 == sorteio.amigos:
      tecla.escreve(tempo = 5, texto = f"@{sorteio.quem_marcar[a]} @{sorteio.quem_marcar[a + 1]}")
    
    elif 3 == sorteio.amigos:
      tecla.escreve(tempo = 5, texto = f"@{sorteio.quem_marcar[a]} @{sorteio.quem_marcar[a + 1]} @{sorteio.quem_marcar[a + 2]}")
    
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
  tecla.botao_direito()
  tecla.esc(tempo=1)
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

def quantos_sigo(eu):
  user_info = request.get(f"https://www.instagram.com/{eu}/?__a=1").json()
  follow_count = user_info["graphql"]["user"]["edge_follow"]["count"]

  return int(follow_count)