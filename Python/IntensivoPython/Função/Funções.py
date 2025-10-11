# Funções e Classes chegaram para organizar e otimizar a criação de código

"""
Funções são o que exatamente ?
R:Uma forma de organizar
codigos soltos em um unico bloco de codigo, que pode ser chamado pelo seu nome

Quando devo usar ?
R: Tem vezes que precisa de fazer algo varias vezes. Em situações assim,
voçe pode tanto criar suas proprias funções ou usar funções disponibilizadas 
pela linguagem de programação que esta usando

"""

# # Função da propria linguagem Exemplo Python :
# print ('Fala Pessoal!') # Resultado : Fala Pessoal!
# round(9.90) # Resultado : 10 arrendonda o valor
# 'calcular_multa'(150)  # Levou multa gravíssima

"""
# Quando devo criar ou usar uma função?
R:Em situações assim,voçe pode tanto criar suas proprias funções ou usar funções disponibilizadas 
pela linguagem de programação que esta usando para agilizar e otimizar a criação de programas.
Ao inves de criar o mesmo codigo varias vezes ao longo do seu programa, crie ou use função para isso.
"""

# Estrutura básica
def eh_maior_de_idade(): # Exemplo de função que processa , porém não retorna algo
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
     print('Voçe e maior de idade')
    else:
     print('Voçe e maior de idade') 

eh_maior_de_idade()

# Crie um algoritmo que permite que maiores de idade entrem na festa
def pode_entrar_na_festa(): # Exemplo de função que processa e retorna algo
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
     return True    
    else:
        return False

if pode_entrar_na_festa()==True:
   print('Bem-vindo a festa')
else:
   print('Voçe não pode entrar')

# Carteira de motorista
def eh_maior_de_idade(possui_cnh): 
    idade = int(input('Digite sua idade: '))
    if idade >= 18 and possui_cnh == True:
     print('Voçe e maior de idade e pode dirigir')
    else:
     print('Voçe não pode dirigir ') 

eh_maior_de_idade (possui_cnh = True)
