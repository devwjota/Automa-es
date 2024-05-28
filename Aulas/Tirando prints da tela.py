# Como tirar print(foto) da tela inteira ou parte dela 
import pyautogui 
# Tirar print da tela inteira
pyautogui.screenshot('tela.jpg')
# Tirar print de uma parte da tela 
pyautogui.screenshot('calculadora.jpg',region=(1226,129,320,530))

