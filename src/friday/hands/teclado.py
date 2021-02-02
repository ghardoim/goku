import pyautogui as auto
import pyperclip as clip
import time as time

def ctrl(letra, shift = ""):
  auto.hotkey("ctrl", shift, letra)

def alt(tab = ""):
  auto.hotkey("alt", tab)

def tecla(letra):
  auto.press(letra)

def esc(tempo):
  time.sleep(tempo)
  auto.press("esc")
  time.sleep(tempo)

def enter(tempo):
  time.sleep(tempo)
  auto.press("enter")
  time.sleep(tempo)

def end(tempo, vezes):
  for end in range(vezes):
    print(end)
    ctrl("end")
    time.sleep(tempo)

def tab(vezes, shift = ""):
  for tab in range(vezes):
    print(tab)
    auto.hotkey(shift, "tab")

def seta(vezes, seta):
  auto.press("numlock")
  for down in range(vezes):
    print(down)
    auto.press(seta)
  auto.press("numlock")

def abre_janela(janela):
  auto.press("win")
  auto.write(janela)
  enter(tempo = 1)

def fecha_janela(tempo):
  time.sleep(tempo)
  auto.hotkey("alt", "f4")
  enter(tempo = 1)

def simula_botao_direito():
  auto.hotkey("shift", "f10")

def escreve(tempo, texto):
  time.sleep(tempo)
  clip.copy(texto)
  ctrl("v")
  clip.copy("")
  time.sleep(tempo)