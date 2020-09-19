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

    nome = tela.Label(self.__master, text = "Qual o seu nome?", fg = "black", bg = "white")
    nome.pack()
    nome = tela.Entry(self.__master, bg = "lightgray")
    nome.pack()

    pagina = tela.Label(self.__master, text = "Qual é a página do sorteio?", fg = "black", bg = "white")
    pagina.pack()
    pagina = tela.Entry(self.__master, bg = "lightgray")
    pagina.pack()

    amigos = tela.Label(self.__master, text = "Quantos amigos você quer marcar por comentário?", fg = "black", bg = "white")
    amigos.pack()
    amigos = tela.Entry(self.__master, bg = "lightgray")
    amigos.pack()

    comentarios = tela.Label(self.__master, text = "Quantos comentários quer fazer?", fg = "black", bg = "white")
    comentarios.pack()
    comentarios = tela.Entry(self.__master, bg = "lightgray")
    comentarios.pack()

    # nome = tela.Label(self.__master, text = "Qual o seu nome?", fg = "black", bg = "white")
    # nome.pack()
    # nome = tela.Entry(self.__master, bg = "lightgray")
    # nome.pack()
