# Como digitar com PyAutoGUI
import pyautogui
import pyperclip # Para usar caracteres especiais

def escrever_frase(frase): # Com essa função 
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl','v')

# Mover o mouse ate o campo de digitar
pyautogui.moveTo(x=822,y=139,duration=2)

# Clicar no campo de digitar
pyautogui.click()

# Digitar minha mensagem
escrever_frase('Olá isso e um teste de Automação')
# para usar com caractere
# pyautogui.typerwrite('Olá isso e um teste de Automação')
# para usar sem caractere

# Clicar no botão de enviar
pyautogui.click(x=822,y=139,duration=2)
