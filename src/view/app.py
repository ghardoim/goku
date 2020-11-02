import src.friday.body.moves as atk
from PIL import ImageTk, Image
import tkinter as tela

class Application(tela.Frame):
  def __init__(self, sorteio, browser, master = tela.Tk()):
    super().__init__(master)
    self.__sorteio = sorteio
    self.__browser = browser
    self.__master = master
    self.inicializa()
    self.imagem()
    self.menu()
  
  def inicializa(self):
    self.__master.title("Oi, eu sou o Goku!")
    self.__master.configure(bg = "white")
    self.__master.maxsize(600, 250)
    self.__master.minsize(600, 250)

  def imagem(self):
    foto = ImageTk.PhotoImage(Image.open("resource/img/goku.png"))
    img = tela.Label(self.__master, image = foto)
    img.image = foto
    img.pack(side = "right")
  
  def menu(self):
    frase = tela.Label(self.__master, text = "Vamos ganhar um sorteio!", fg = "black", bg = "white")
    frase.pack(side = "top")

    # nome = self.cria_input("Qual o seu nome?")
    # pagina = self.cria_input("Qual é a página do sorteio?")
    # amigos = self.cria_input("Quantos amigos você quer marcar por comentário?")
    # comentarios = self.cria_input("Quantos comentários quer fazer?")
    
    atualizar = self.cria_botao("Atualizar lista de amigos", lambda: atk.kaioken(self.__browser, self.__sorteio))
    espaco = self.cria_input("---------------------------------------------------------------------------------")
    marcar = self.cria_botao("Marcar amigos", lambda: atk.kamehameha(self.__browser, self.__sorteio))

  def cria_input(self, mensagem):
    frame = tela.Frame(self.__master, width = 100, height = 100)
    campo = tela.Label(frame, text = mensagem, fg = "black", bg = "white")
    campo.pack(side = "left")
    campo = tela.Entry(frame, bg = "lightgray")
    campo.pack(side = "left")
    frame.pack()
    return frame

  def cria_botao(self, mensagem, funcionalidade):
    campo = tela.Button(self.__master, text = mensagem, command = funcionalidade, width = 20, height = 5)
    campo.pack(side = "top")

    return campo
