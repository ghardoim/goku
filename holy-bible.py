#!/usr/bin/env python
# -*- coding: utf-8 -*-

from src.friday.hands import teclado as tecla
from src.friday.hands import mouse as mouse


palavras_por_linha = int(6)
intervalo_de_tempo = 0.2
tecla.alt(tab = "tab")

for livro in biblia:
  livro_nome = livro["name"]

  if not livro_nome in [""]:
    n_Capitulo = 1
    for capitulo in livro["chapters"]:

      # if "Josué" == livro_nome and 14 > n_Capitulo:
      #   n_Capitulo += 1
      #   continue

      print(f"{livro_nome} {n_Capitulo}")

      tecla.esc(tempo = 1)
      tecla.alt(tab = "n")
      tecla.tecla("x")
      tecla.escreve(tempo = intervalo_de_tempo, texto = f"{livro_nome} {n_Capitulo}")
      tecla.tab(1)

      mouse.clica(490, 110, tempo = 0.5)
      mouse.clica(590, 110, tempo = 0.5)
      mouse.duplo_clique(215, 185, tempo = 0.5)

      n_Versiculo = 1
      for versiculo in capitulo:

        palavras_do_versiculo = versiculo.split(" ")
        
        print()
        print(f"{n_Versiculo}", end = ". ")
        tecla.escreve(tempo = intervalo_de_tempo, texto = f"{n_Versiculo}. ")

        for x in range(0, len(palavras_do_versiculo), palavras_por_linha):
          [print(palavra, end = " ") for palavra in palavras_do_versiculo[x : x + palavras_por_linha]]
          
          [tecla.escreve(tempo = intervalo_de_tempo, texto = f"{palavra} ") for palavra in palavras_do_versiculo[x : x + palavras_por_linha]]
          tecla.enter(tempo = intervalo_de_tempo)
          
          print()

        tecla.enter(tempo = 0)

        n_Versiculo +=1
        
      tecla.esc(tempo = 0)
      tecla.enter(tempo = 2)

      n_Capitulo += 1