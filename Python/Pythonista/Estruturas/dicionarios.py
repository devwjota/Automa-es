# Dicionarios
'''
Pessoa
    nome
    idade
    altura
'''
# Dicionario(chave,valor)
dicionario_pessoa = {'nome':'Wanderson','idade':21,'altura':1.82}
# pessoa_2 = dict(nome ='Carol',idade=18,altura=1.60)
# print(dicionario_pessoa.keys())
# print(dicionario_pessoa.values())
# print(dicionario_pessoa.items())

#Iterar sobre um dicionario
for item in dicionario_pessoa.items():
    print(item)
    print(item[1])
