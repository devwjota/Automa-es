# Set 
frutas ={'maça','uva','banana','maça','morango'}
numeros = [2,2,5,8]
# Convertendo para set
set_numeros = set(numeros)
set_frutas = set(frutas)

# print(set_numeros)
print(set_numeros)
print(set_frutas)

# adicionando novos valores
set_numeros.add(10)
print(set_numeros)

# Conjuntos
numero1 = [2,2,5,8]
numero2 = [2,2,3,9]
a = set(numero1)
b = set(numero2)
print(a.symmetric_difference(b))
print(a.intersection(b))
print(a.union(b))

