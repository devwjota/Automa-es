import pyautogui
from time import sleep
import pyperclip
def login_senha(senha): # no meu caso tem caractere
    pyperclip.copy(senha)

# Abrir o Google Chrome
pyautogui.moveTo(269,878,duration=2)
pyautogui.click()
sleep(1)
# Aperta na aba de pesquisar
pyautogui.moveTo(247,62,duration=3)
pyautogui.click()
sleep(1)
# Digitar hotmail na aba de pesquisar
pyautogui.typewrite('https://hotmail.com/')
pyautogui.hotkey('enter')
# Aceitar cookies
# Clicar no campo de entrar
pyautogui.moveTo(1446,112,duration=3)
pyautogui.hotkey(button='left')
pyautogui.click()
sleep(1)
# Navegar e clicar no campo email
pyautogui.moveTo(772,450,duration=3)
pyautogui.click()
sleep(1)
# # Digitar o email
pyautogui.typewrite('email')
# Aperta em avançar
pyautogui.moveTo(915,562,duration=3)
pyautogui.click()
sleep(1)
# Campo de senha
pyautogui.click(693,489,duration=3)
# Digitar minha senha
login_senha('senha')
pyautogui.hotkey('ctrl','v')
# Entrar apos colocar a senha
pyautogui.moveTo(916,617,duration=3)
pyautogui.hotkey('enter')
# Salvar senha se quiser
# pyautogui.moveTo(1327,362,duration=3)
# pyautogui.click()
# Continuar conectado ?
pyautogui.moveTo(922,603,duration=3)
pyautogui.click()
