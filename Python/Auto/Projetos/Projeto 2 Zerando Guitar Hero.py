import pyautogui
import keyboard
from time import sleep

"""
Entender os passos manuais do jogo depois cria o código

Verificar se  há um botão com a cor correspondente dentro
do circulo daquela cor 
""" 
while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(950, 711, (0, 152, 0)):# Verde
        pyautogui.press('a')
        #sleep(0.02)

    if pyautogui.pixelMatchesColor(1043,711, (255,0,0)):# Vermelho
        pyautogui.press('s')
        #sleep(0.02)

    if pyautogui.pixelMatchesColor(1130,709, (244,244,2)): # Amarelo
        pyautogui.press('j')
        #sleep(0.02)

