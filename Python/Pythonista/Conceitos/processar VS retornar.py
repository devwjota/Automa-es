# Processar VS Retornar
# Função que apenas processa dados 
# print('Ola!')
# Funções que retorna dados 
# cidade = input('Qual e a sua cidade? :')
# Como escolher entre funções que processam VS retornam dados ?
'''Eu vou precisar de usar essa informação na logica do meu programa ainda? Ou so
preciso processa esse dado,mas nao irei utilizar mais ele depois?'''
def exibir_cotação_do_dia(moeda):
    if moeda == 'usd':
        print(5.47)

exibir_cotação_do_dia('usd')

def obter_cotação_do_dia(moeda):
    if moeda =='usd':
        return 5.47 #True, Valores booleanos,inteiros , strings
    
cotação = obter_cotação_do_dia('usd')
if cotação >5:
    print('Investir em ações americanas')
else:
    print('Cotação não favoravel')
    

