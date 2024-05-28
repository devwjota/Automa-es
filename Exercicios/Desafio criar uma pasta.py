import pyautogui

pyautogui.click(x=1337,y=379,clicks=1,
interval=0.1,button='left',duration=2)

pyautogui.click(x=1337,y=379,clicks=1,
interval=0.1,button='right',duration=2)

pyautogui.click(x=1375,y=664,clicks=1, #novo
interval=0.1,button='left',duration=2)

pyautogui.click(x=1099,y=387,clicks=1, #pasta
interval=0.1,button='left',duration=2)


# Solução do professor 
import pyautogui

pyautogui.rightClick(x=...,y=...,duration=2) 
pyautogui.move(x=...,y=...,duration=2)
pyautogui.move(x=...,y=...,duration=2)
pyautogui.click()