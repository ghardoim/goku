import teclado as tecla
import time as time

def marca(amigos, qnt_de_comentarios, qnt_amigos_por_comentario):

  for a in range(0, (qnt_amigos_por_comentario * qnt_de_comentarios) - 1, qnt_amigos_por_comentario):

    if 1 == qnt_amigos_por_comentario:
      tecla.escreve(2, "{}".format(amigos[a]))
    
    elif 2 == qnt_amigos_por_comentario:
      tecla.escreve(2, "{} {}".format(amigos[a], amigos[a + 1]))
    
    elif 3 == qnt_amigos_por_comentario:
      tecla.escreve(2, "{} {} {}".format(amigos[a], amigos[a + 1], amigos[a + 2]))
    
    tecla.tab(1, "")
    tecla.enter(1)
    time.sleep(5)
    tecla.tab(2, "shift")