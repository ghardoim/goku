from PIL import ImageTk, Image
import tkinter as tela

class Application(tela.Frame):
  def __init__(self, master = tela.Tk()):
    super().__init__(master)
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
    foto = ImageTk.PhotoImage(Image.open("img/goku.png"))
    img = tela.Label(self.__master, image = foto)
    img.image = foto
    img.pack(side = "right")
  
  def menu(self):
    frase = tela.Label(self.__master, text = "Vamos ganhar um sorteio!", fg = "black", bg = "white")
    frase.pack(side = "top")

    nome = self.cria_input("Qual o seu nome?")
    pagina = self.cria_input("Qual é a página do sorteio?")
    amigos = self.cria_input("Quantos amigos você quer marcar por comentário?")
    comentarios = self.cria_input("Quantos comentários quer fazer?")

  def cria_input(self, mensagem):
    campo = tela.Label(self.__master, text = mensagem, fg = "black", bg = "white")
    campo.pack()
    campo = tela.Entry(self.__master, bg = "lightgray")
    campo.pack()
    return campo
