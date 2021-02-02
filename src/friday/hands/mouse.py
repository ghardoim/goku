import pyautogui as auto
import time as time

def vai_pro_canto():
  auto.moveTo(1, 1)

def clica(x, y, tempo = 0):
  time.sleep(tempo)
  auto.click(x, y)

def duplo_clique(x, y, tempo = 0):
  time.sleep(tempo)
  auto.doubleClick(x, y)