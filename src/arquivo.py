def le_info(path):
  with open(path, "r") as arquivo:
    if "amigos.txt" not in path:
      return arquivo.readline()
    else:
      amigos = []
      for nome in arquivo:
        amigos.append("@{}".format(nome.strip()))
      return amigos