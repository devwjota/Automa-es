import pyautogui
from time import sleep

# Posição de algo -  use o MouseInfo
# Fazer algo com essa posição
pyautogui.moveTo(1223,302,duration=2)
# pyautogui.move(0,-50,duration=2)
for i in range(5000):
    sleep(0.1)
    pyautogui.click() # Para parar a execução: CTRL + C ou joga o mouse para esquerda rapidamente