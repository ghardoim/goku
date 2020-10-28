import src.friday.hands.teclado as tecla

def procura(texto, tempo):
  tecla.ctrl("f")
  tecla.escreve(tempo, texto)
  tecla.enter(tempo)
  tecla.esc(tempo)