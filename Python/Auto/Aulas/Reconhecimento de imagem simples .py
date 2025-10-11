# Reconhecimento de imagem simples com pyautogui
import pyautogui

# Encontrar asa coordenadas próximas de onde aquela imagem está
print(pyautogui.locateOnScreen('nome.tipo de arquivo'))

# Encontrar a coordenada do centro de uma imagem
print(pyautogui.locateCenterOnScreen('nome.tipo de arquivo'))

# Como usar na prática
pyautogui.click(x=...,y=...,duration=2)

captcha = pyautogui.locateCenterOnScreen('recapcha.png')
pyautogui.click(captcha[0],captcha[1],duration=2)