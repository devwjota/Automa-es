# Coleções(listas)

# Lista 
preços = [20,50,200] # acessar o por indices 0,1,2,3...
print(preços[2])
print(preços.index(200)) # 'index' mostra qual e o indice 

# Lista 2
diversidades = [15,'Wanderson',True,9.5]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])
print(diversidades[3])

# Lista em iteráveis laços de repetição
for preço in preços:
    print(preço)

# Exemplo 5 - Some os valores
'''
Dados uma  coleção de dados "idades" [15,46,75,34,23]
imprima na tela a soma deste valores

idades = [15,46,75,34,23]
total = 0
loop idade em idades
    total = total + idade
print total
'''
idades = [15,46,75,34,23]
total = 0
for idade in idades:
    total = total + idade
print(total)