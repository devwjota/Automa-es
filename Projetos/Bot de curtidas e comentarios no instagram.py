from time import sleep
import datetime
import threading
import pyautogui
import webbrowser

def sair():
    pyautogui.click(1553,141, duration=1)
    pyautogui.click(36,811, duration=1)
    pyautogui.click(44,741, duration=1)

def login():
    # Navegar até o site : https://www.instagram.com/
    webbrowser.open_new_tab('https://www.instagram.com')
    sleep(1.5)
    
    # Colocar usuário
    pyautogui.click(944, 322, duration=1)
    pyautogui.typewrite('usuario')
    sleep(1)

    # Colocar Senha
    pyautogui.click(931, 367, duration=1)
    pyautogui.typewrite('senha')
    sleep(1)

    # Clicar em entrar
    pyautogui.click(991, 412, duration=1)
    sleep(1.5)

    # Caso peça para salvar a senha do Instagram
    pyautogui.click(910, 539, button='left', duration=1)  # Agora não
    sleep(1.5)

    # Clicar na barra de pesquisar
    pyautogui.click(67, 293, duration=1)
    sleep(1)

    # Pesquisar a página no Instagram
    pyautogui.click(161, 235, duration=1)
    sleep(1)
    pyautogui.typewrite('fluminense')
    sleep(1)

    # Entrar na página
    pyautogui.click(179, 290, duration=1)
    sleep(1)

    pyautogui.click(597,711, duration=1)
    sleep(1)

    # Verificar se já está curtido
    curtido = (255, 48, 64)
    cord = (844, 700)
    cord_pixel = pyautogui.pixel(*cord) # " * " para duplicar 
    pyautogui.moveTo(cord, duration=1)

    if cord_pixel == curtido:
        print('Já está curtido')
        coment_insta()
        rodar_24_horas()

    else:
        print('Não curtido, curtindo agora')
        pyautogui.click(cord, duration=1)
        sleep(1)
        coment_insta()
        rodar_24_horas()
      

def coment_insta():
    cord_coment = (886,704)
    pyautogui.click(cord_coment, duration=1)
    sleep(1)

    
    pyautogui.typewrite('flu')
    sleep(1)
    pyautogui.click(1273,804)
    sleep(1)
    sair()

 
def rodar_24_horas():
    agora = datetime.datetime.now()
    proxima_execucao = agora + datetime.timedelta(hours=24)
    print(f'Rodou às {agora}, vai rodar novamente às {proxima_execucao}')
    threading.Timer(24 * 60 * 60, login).start()

login()  # Inicia a execução imediatamente