def exibir_preço(*,nome_produto,preço):
    print(f'{nome_produto}esta no valor de {preço}')

# Argumentos posicionais
exibir_preço(nome_produto='Iphone',preço=5000)

# Argumentos nomeados
exibir_preço(preço=5000, nome_produto='Iphone') # Pra tornar uma palavra ou numero em nomeado tem que colocar ,*, antes da (coisa que colocar )

# Desafio 🥇
'''
Crie uma função chamado gerar_objeto_personalizado que irá receber 3 parâmetros, cor, altura, formato.
A sua função deve apenas imprimir na tela o que foi passado para ela, nada mais, nada menos.
Porém ela deve seguir as seguintes regras:
1 - O primeiro argumento deve ser posicional
2 - Os argumentos altura e formato precisam OBRIGATORIAMENTE serem nomeados
'''
def gerar_objeto_personalizado(cor_do_objeto,*,altura,formato):
    print(cor_do_objeto, altura, formato)

gerar_objeto_personalizado('Verde',altura=1.92,formato='retangulo')


# Crie uma função que descreva o patrocinio master do fluminense , preço da camisa e quantidades 
def produto_master (patrocinio,*,preço_da_camisa,quantidade):
    print(patrocinio,preço_da_camisa,quantidade)
produto_master('SuperBet',preço_da_camisa='R$369,90',quantidade='20.000 unidades') 










