# DESAFIO 🥇
import pyautogui
import webbrowser
from time import sleep

# 1) Navegue até o site https://cursoautomacao.netlify.app/
webbrowser.open_new_tab('https://cursoautomacao.netlify.app/')

# 2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
pyautogui.click(1208,211,duration=2)
for i in range(2):
    pyautogui.scroll(-300)
    sleep(0)
# Pegar a coordenada, Digitar o nome
pyautogui.click(1280,616,duration=2)
pyautogui.typewrite('Wanderson Junior')
# # Colar no campo de "Digitar nome"
pyautogui.hotkey('ctrl','v')

# 3) Clique em alerta, para gerar a alerta
# # Pegar a coordenada 
pyautogui.click(1224,652,duration=1.5)

# 4) Feche a alerta
pyautogui.click(966,187,duration=1.5)

# 5) Suba a página totalmente para cima
for i in range(2):
    pyautogui.scroll(500)
    sleep(2)



'''
6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos 
para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
'''
for i in range(2):
    pyautogui.scroll(-780)
# Clicar no botão de download do excel
pyautogui.click(313,723,duration=2)
sleep(1)
# Selecionar o link do site que foi a forma que eu achei
pyautogui.hotkey(button='F6')
sleep(1)
# Clicar no botão de download de pdf
pyautogui.click(493,726)
sleep(1)

# 7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
pyautogui.alert(text='VOCÊ TERMINOU 😎',title=
'Automação Concluida! ✔',button='ok')