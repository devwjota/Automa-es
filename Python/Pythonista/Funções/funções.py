# # Funções 
# input()
# len()
# split()

'''
def nome_da_função(paramentros):
    comandos
'''
# def dar_boas_vindas(): # sem parametro (vazio)
#     print('Bem-vindo!')
# dar_boas_vindas()

# def dar_boas_vindas_personalizada(nome): # com parametro
#     print(f'Bem-vindo(a) {nome}!')
# dar_boas_vindas_personalizada('Wanderson')


# Valor padrão
# def apresentar_lugar(horario_de_funcionamento,Lugar ='Nossa Loja'):
#     print(f'Conheça {Lugar},Horario de funcionamento das {horario_de_funcionamento}')
# apresentar_lugar('08:00 as 18:00','Loja de Eletronicos')


# Desafio🥇

# DESAFIO 1 - Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome e sobrenome de alguém e dá boas vindas para essa pessoa
def gerar_nome_completo(nome='Wanderson',sobrenome='Junior'):
    print(f'Bem-vindo  {nome} {sobrenome}!')
gerar_nome_completo()

# DESAFIO 2 - # Crie uma função chamada calcular_valores que recebe 2 parâmetros o primeiro o preco de um produto e o segundo parâmetro é a quantidade,
# porém a quantidade deve haver um valor padrão de 1. Sua função deve exibir o resultado do preço do produto, multiplicado a quantidade escolhida.
def calcular_valores (preço_de_um_produto =(4) ,quantidade_de_um_produto=3):
    print(f'{preço_de_um_produto * quantidade_de_um_produto}')
calcular_valores()

