import json as json

class Sorteio():
  def __init__(self, informacoes):
   
    with open(informacoes) as arquivo:
      sorteio = json.load(arquivo)
      self.__eu = sorteio["eu"]
      self.__pagina = sorteio["pagina"]
      self.__publicacao = sorteio["publicacao"]
      self.__comentarios = sorteio["comentarios"]
      self.__amigos = sorteio["amigos"]
      self.__quem_marcar = sorteio["quem_marcar"]
  
  def __iter__(self):
    return iter(self)

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
  def quem_marcar(self):
    return self.__quem_marcar

  @quem_marcar.setter
  def quem_marcar(self, nomes):
    self.__quem_marcar = nomes
  
  @property
  def toJson(self):
    return {
      "eu": self.eu,
      "pagina": self.pagina,
      "publicacao": self.publicacao,
      "comentarios": self.comentarios,
      "amigos": self.amigos,
      "quem_marcar": self.quem_marcar
    }

  @property
  def salvar(self):
    with open("sorteio.json", "w") as arquivo:
      json.dump(self.toJson, arquivo)

  def __str__(self):
    return f"Vou marcar {self.amigos} pessoa(s) em cada um dos {self.comentarios} comentário(s) que vou fazer na {self.publicacao}° publicação da página '{self.pagina}'"