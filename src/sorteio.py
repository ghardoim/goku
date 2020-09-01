import json as json

class Sorteio:
  def __init__(self, informacoes):
    with open(informacoes, "r") as arquivo:
      sorteio = json.load(arquivo)
      self.__eu = sorteio["eu"]
      self.__pagina = sorteio["pagina"]
      self.__publicacao = sorteio["publicacao"]
      self.__comentarios = sorteio["comentarios"]
      self.__amigos = sorteio["amigos"]
      self.__marcar = sorteio["marcar"]

  @property
  def eu(self):
    return self.__eu

  @property
  def pagina(self):
    return self.__pagina

  @property
  def publicacao(self):
    return self.__publicacao
  
  @property
  def comentarios(self):
    return self.__comentarios
  
  @property
  def amigos(self):
    return self.__amigos
  
  @property
  def marcar(self):
    return self.__marcar

  def __str__(self):
    return f"Vou marcar {self.amigos} pessoa(s) em cada um dos {self.comentarios} comentário(s) que vou fazer na {self.publicacao}° publicação da página '{self.pagina}'"