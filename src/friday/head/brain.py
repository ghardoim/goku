from src.model.relogio import Relogio
import os as os

relogio = Relogio()

def entenda(texto):
  # entendi = ""

  # if len(texto.split()) < 3:
  #   entendi = "Você falou muito pouco"

  if procure("dia", texto):
    return { "fala" : "Hoje é dia de PGM aviva! O melhor que nós temos!", "tipo" : 2}

  elif procure("pesquise", texto):
    return { "fala" : "Vou pesquisar isso!", "tipo" : 1 } 
  # elif "!" in texto:
  #   entendi = "Essa afirmação é interessante"
  
  # elif "até" in texto or "sair" in texto or "desligar" in texto:
  #   entendi = "Até mais!"

  # else:
  #   entendi = "O que você quis dizer com isso?"
  # return resposta_gentil("bom", texto)

def procure(algo, texto):
  for palavra in texto.split():
    if algo in palavra.lower():
      return True

def hello():
  return f"{relogio.hello_world}, {os.getlogin()} {relogio}"