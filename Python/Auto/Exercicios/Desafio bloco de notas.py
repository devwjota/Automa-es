import pyautogui
import pyperclip

def automaçao_e_brabo(bloco):
    pyperclip.copy(bloco)

pyautogui.moveTo(x=822,y=139,duration=2)
pyautogui.click()

automaçao_e_brabo('Automação é Incrível!')
pyautogui.hotkey('ctrl','v')

pyautogui.click(x=822,y=139,duration=2)
