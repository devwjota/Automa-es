# Trabalhar com multiplas listas
from itertools import zip_longest

# a_lista=['A','B','C','D','E']
# b_lista=[1,2,3,4,5]

# for a, b in zip(a_lista, b_lista):
#     print(a)
#     print(b)

# produtos =['produto 1','produto 2','produto 3','produto 4']
# precos =[250,150,220,550,50]
# for a, b in zip(produtos,precos):
#     print(f'Salvando produto {a} valor R$ {b}')

# titulos = ['Copa do Brasil','Brasileiro','Brasileiro','Libertadores']
# descricao =['2007','2010','2012','2023']

# for titulo, descricao in zip_longest(titulos, descricao):
#     print(f'Fluminense foi campeão nos seguintes anos {descricao} conquistando os seguintes {titulo}')


# DESAFIOS 🥇

# DESAFIO 1

# Usando as listas abaixo:
p_lista= ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
r_lista = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']

for p, r in zip(p_lista, r_lista): # p:'produto',r:'real'
    print(p)
    print(r)

produtos = ['Produto 1', 'Produto 2', 'Produto 3', 'Produto 4', 'Produto 5']
precos = ['R$500,00', 'R$1500,00', 'R$2700,00', 'R$5000,00']

for p, r in zip (produtos,precos):
    print(f'Salvando produto {p} valor R$ {r}')



