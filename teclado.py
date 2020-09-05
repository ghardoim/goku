import pyautogui as auto
import time as time

def ctrl(letra):
  auto.hotkey("ctrl", letra)

def esc():
  auto.press("esc")

def end():
  auto.hotkey("ctrl", "end")

def enter(tempo):
  time.sleep(tempo)
  auto.press("enter")
  time.sleep(tempo)

def tab(vezes, shift):
  for tab in range(vezes):
    auto.hotkey(shift, "tab")

def down(vezes):
  auto.press("numlock")
  for down in range(vezes):
    auto.press("down")
  auto.press("numlock")

def abre_janela(janela):
  auto.press("win")
  auto.write(janela)
  enter(tempo = 1)

def fecha_janela(tempo):
  time.sleep(tempo)
  auto.hotkey("alt", "f4")
  enter(tempo = 1)

def botao_direito(tempo):
  auto.hotkey("shift", "f10")
  time.sleep(tempo)
  esc()
  time.sleep(tempo)
  auto.hotkey("shift", "f10")

def escreve(tempo, texto):
  time.sleep(tempo)
  auto.write(texto)
  time.sleep(tempo)