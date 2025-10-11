from time import sleep
import webbrowser
import pyautogui

# Escolher um contato
# Enviar msg para esse contato
'https://api.whatsapp.com/send?phone=.....'
# Repetir isso para outros contatos
telefones= ['telefones']

for telefone in telefones:
    webbrowser.open(f'https://api.whatsapp.com/send?phone={telefone}')
    sleep(5)
    pyautogui.click(1226,252, duration=1)
    sleep(5)
    pyautogui.typewrite('Gostaria de participar do nosso evento?(digite sim, se gostaria de participar.)')
    sleep(5)
    pyautogui.press('enter')
    sleep(200)


