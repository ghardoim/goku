import instagram as insta
import pyautogui as auto
import teclado as tecla
import arquivo as file
import time as time

numero_da_publicacao_do_sorteio = int(file.le_info("resource/numero_publicacao.txt"))
qnt_de_amigos_por_comentario = int(file.le_info("resource/amigos_por_comentario.txt"))
qnt_de_comentarios = int(file.le_info("resource/qnt_de_comentarios.txt"))
pagina_do_sorteio = file.le_info("resource/pagina_sorteio.txt")
browser = file.le_info("resource/navegador.txt")
amigos = file.le_info("resource/amigos.txt")

def kamehameha():
  print("Oi, eu sou o Goku!")
  time.sleep(1)
  print("Levante as mãos e me ajude a fazer a genki dama enquanto eu faço uns comentários para vc!")
  time.sleep(2)
  print("Eu vou marcar {} amigos em {} comentários na {}° publicação da página {}, tudo bem??"
    .format(qnt_de_amigos_por_comentario, qnt_de_comentarios, numero_da_publicacao_do_sorteio, pagina_do_sorteio))
  time.sleep(2)
  print("Vou comentar todos esses seus amigos aqui ->")
  for amigo in amigos:
    time.sleep(1)
    print("\t", amigo)
  print("O meu KI ainda não está bom, mas vou continuar treinando para melhorar isso!!")
  time.sleep(1)
  input("Aperte 'enter' e me dê a mão pra fugir desta terrível escuridão")

  tecla.abre_janela(browser)
  tecla.enter_ctrl(1, "l")
  tecla.escreve(1, "instagram.com/{}/".format(pagina_do_sorteio))
  tecla.enter_ctrl(2, "f")
  tecla.escreve(1, "publicacoes")
  tecla.enter(2)
  tecla.esc()
  tecla.tab(2 + numero_da_publicacao_do_sorteio, "")
  tecla.enter(2)
  tecla.tab(2, "shift")
  insta.marca(amigos, qnt_de_comentarios, qnt_de_amigos_por_comentario)
  tecla.tab(1, "")
  tecla.esc()
  tecla.fecha_janela(1)

if __name__ == "__main__":
  kamehameha()