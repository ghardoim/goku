import navegador as navegador
from sorteio import Sorteio
import instagram as insta
import teclado as tecla
import mouse as mouse

sorteio = Sorteio("sorteio.json")
browser = "edge"
mouse.vai_pro_canto()

def kaioken():

  print("Oi, eu sou o Goku!")
  print(r"                    `\-.   `                                         ")
  print(r"                      \ `.  `                                        ")
  print(r"                       \  \ |                                        ")
  print(r"              __.._    |   \.                                        ")
  print(r"       ..---~~     ~ . |    Y                                        ")
  print(r"         ~-.          `|    |                                        ")
  print(r"            `.               `~~--.                                  ")
  print(r"              \                    ~.                                ")
  print(r"               \                     \__. . -- -  .                  ")
  print(r"         .-~~~~~      ,    ,            ~~~~~~---...._               ")
  print(r"      .-~___        ,'/  ,'/ ,'\          __...---~~~                ")
  print(r"            ~-.    /._\_( ,(/_. 7,-.    ~~---...__                   ")
  print(r"           _...>-  P""6=`_/\"6\"~   6)    ___...--~~~                ")
  print(r"            ~~--._ \`--') `---'   9'  _..--~~~                       ")
  print(r"                  ~\ ~~/_  ~~~   /`-.--~~                            ")
  print(r"                    `.  ---    .'   \_                               ")
  print(r"                      `. \" _.-'     | ~-.,-------._                  ")
  print(r"                  ..._../~~   ./       .-'    .-~~~-.                ")
  print(r"            ,--~~~ ,'...\` _./.----~~.'/    /'       `-              ")
  print(r"        _.-(      |\    `/~ _____..-' /    /      _.-~~`.            ")

  print("Estou treinando uma nova técnica!")
  print("Que tal se eu te ajudar a achar amigos para você marcar??")
  input("Aperte 'enter' e me dê a mão pra fugir desta terrível escuridão!!")
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

def kamehameha():

  print("Oi, eu sou o Goku!")
  print("Levante as mãos e me ajude a fazer a genki dama enquanto eu faço uns comentários para vc!")
  print(sorteio)
  print("Vou comentar todos esses seus amigos aqui ->")
  for amigo in sorteio.quem_marcar:
    print("\t", amigo)
  print("O meu KI ainda não está bom, mas vou continuar treinando para melhorar isso!!")
  input("Aperte 'enter' e me dê a mão pra fugir desta terrível escuridão")

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

if __name__ == "__main__":
  # pass
  #kamehameha()
  kaioken()