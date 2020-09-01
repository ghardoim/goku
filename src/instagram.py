import teclado as tecla
import time as time

def marca(amigos, qnt_comentarios, por_comentario):

  for a in range(0, (por_comentario * qnt_comentarios) - 1, por_comentario):

    if 1 == por_comentario:
      tecla.escreve(tempo = 5, texto = f"@{amigos[a]} desculpe o incômodo! estou testando o Goku! :D")

    elif 2 == por_comentario:
      tecla.escreve(tempo = 5, texto = f"{amigos[a]} {amigos[a + 1]}")
    
    elif 3 == por_comentario:
      tecla.escreve(tempo = 5, texto = f"{amigos[a]} {amigos[a + 1]} {amigos[a + 2]}")
    
    tecla.tab(1, "")
    tecla.enter(tempo = 1)
    time.sleep(20)
    tecla.tab(2, "shift")