import teclado as tecla
import time as time

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