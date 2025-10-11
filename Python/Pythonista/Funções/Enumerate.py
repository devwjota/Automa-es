# Enumerate 
# for indice, numero in enumerate(range(1,11, 1)):
#     print(indice, numero)
#     if indice == 5:
#         print('Estamos na metade da lista')


# nomes =['German Cano','John Arias','Ganso','Felipe Melo','Fabio']
# for indice, nomes in enumerate(nomes, 1 ):
#     print(indice, nomes)
#     if indice == 3:
#         print('O maestro chegou !!!')



# Desafio
'''
 Itere sobre a lista abaixo o numero de indice + nome da fruta. 
 Porem quando o indice for 3 exiba 'N' indice + nome da fruta em Promoção

''' 
# frutas = ['Maçã','Laranja','Morango','Limão']
# for indice, frutas in enumerate(frutas):
#     print(indice, frutas)
#     if indice == 3:
#         print('O limão esta em promoção !!!')



# Resolução professor 
frutas = ['Maçã','Laranja','Morango','Limão']
for indice , fruta in enumerate(frutas, 0):
    if indice == 3:
        print(f'{indice} {fruta} EM PROMOÇÃO')
    else:
        print(indice , fruta)

