import pyautogui

pyautogui.alert(text='Iniciando sua Automação',title=
'Automação de login',button='ok') # Alerta  para o usuario                        
 
# Pedir informação
# Email
email = pyautogui.prompt(text='Digite seu email',title=
'informações obrigatórias')
print(f'voçe digitou {email}')

# Confirmar se algo deve ou não acontecer
resposta=pyautogui.confirm(text='Continuar rodando nossa automação?',title='confirmação',buttons=['Sim', 'Não', 'Cancelar'])
if resposta =='sim':
    print('continuando automação')
elif resposta =='não':
    print('encerrando automação')
else:
    print('operação cancelada')

# Senha
senha = pyautogui.password(text='digite sua senha:',title='dados de login',mask='*')
print(senha)
    


