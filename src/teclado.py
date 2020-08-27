import pyautogui as auto
import time as time

def ctrl(letra):
  auto.hotkey("ctrl", letra)

def enter(tempo):
  time.sleep(tempo)
  auto.press("enter")
  time.sleep(tempo)

def enter_ctrl(tempo, letra):
  enter(tempo)
  ctrl(letra)

def tab(vezes, shift):
  for tab in range(vezes):
    auto.hotkey(shift, "tab")

def esc():
  auto.press("esc")

def fecha_janela(tempo):
  time.sleep(tempo)
  auto.hotkey("alt", "f4")

def abre_janela(janela):
  auto.press("win")
  auto.write(janela)

def escreve(tempo, texto):
  time.sleep(tempo)
  auto.write(texto)
  time.sleep(tempo)