# Como pegar e "arrastar" algo para outro lugar
import pyautogui

for i in range(7): # laço de repetição for e range para repetir 'x' vezes
    pyautogui.moveTo(1847,136,duration=1) # o ponto que vai mover
    pyautogui.dragTo(2472,320,button='left',duration=1) # pra onde vai arrastar e qual botão vai apertar
    pyautogui.click(2823,471,duration=1) # o ponto que vai executar o click



