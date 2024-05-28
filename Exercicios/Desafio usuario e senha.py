import pyautogui
from time import sleep

# Pedir informação

# Email
email = pyautogui.prompt(text='Digite seu Email😁',title=
'Digite seu Login e Senha')
print(f'voçe digitou {email}')
pyautogui.moveTo(807,121,duration=2)
pyautogui.click(button='left')
pyautogui.typewrite(f'{email}')
pyautogui.hotkey('ctrl','v')
# Senha
senha = pyautogui.password(text='digite sua senha:',title='Digite sua Senha🐱‍👤',mask='*')
print(senha)
pyautogui.hotkey('enter')
pyautogui.typewrite(senha)