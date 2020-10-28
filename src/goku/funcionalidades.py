from src.controller import navegador, insta
import src.friday.hands.teclado as tecla

def kaioken(browser, sorteio):

  tecla.abre_janela(browser)
  tecla.ctrl("l")
  tecla.escreve(tempo = 3, texto = f"instagram.com/{sorteio.eu}/")
  tecla.enter(tempo = 2)
  navegador.procura("seguindo", tempo = 2)
  quantidade = insta.quantos_sigo(sorteio.eu)
  tecla.enter(tempo = 1)
  insta.carrega_amigos()
  navegador.procura("seguindo", tempo = 2)
  tecla.enter(tempo = 1)
  sorteio.quem_marcar = insta.get_amigos(quantos = quantidade)
  sorteio.salvar

def kamehameha(browser, sorteio):

  tecla.abre_janela(browser)
  tecla.ctrl("l")
  tecla.escreve(tempo = 5, texto = f"instagram.com/{sorteio.pagina}/")
  tecla.enter(tempo = 3)
  tecla.ctrl("f")
  tecla.escreve(3, "publicacoes")
  tecla.enter(tempo = 3)
  tecla.esc(tempo = 1)
  insta.acha_sorteio(sorteio.publicacao)
  insta.marca(sorteio)
  tecla.tab(1)
  tecla.esc(tempo = 1)
  tecla.fecha_janela(tempo = 1)