from datetime import datetime as data

class Relogio():
  def __init__(self):
    
    self.__semana = ["domingo", "segunda", "terça", "quarta", "quinta", "sexta", "sábado"]
    self.__ano = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

  def __me_informe(self, formato):
    return int(data.now().strftime(formato))

  @property
  def horas(self):
    return self.__me_informe("%H")

  @property
  def hoje_dia_mes(self):
    return self.__me_informe("%d")

  @property
  def hoje_dia_semana(self):
    return self.__semana[self.__me_informe("%w")]
  
  @property
  def hoje_mes_ano(self):
    return self.__ano[self.__me_informe("%m")]
  
  @property
  def hello_world(self):
    if self.horas <= 12 and self.horas > 6:
      return "bom dia"
    elif self.horas <= 18 and self.horas > 12:
      return "boa tarde"
    else:
      return "boa noite"

  def __str__(self):
    return f"hoje é {self.hoje_dia_semana}, dia {self.hoje_dia_mes} de {self.hoje_mes_ano} e são {self.horas} horas"