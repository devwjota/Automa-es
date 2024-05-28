# Como usar a função click
import pyautogui
# Click personalizado
pyautogui.click(x=1252,y=528,clicks=1000,
interval=0.1,button='left',duration=2)

# Click na posição atual(com botão esquerdo)
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui.click(button='middle')
# Clicar X vezes
pyautogui.click(clicks=10)
# Funções prontas para clicks
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()
pyautogui.tripleClick() # Geralmente nunca e usado mas e bom saber