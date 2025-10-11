# Valores aleatorios com random
import random
print(random.random()) # Gera um valor de 0.0 a 1.0

# Gera um valor decimal de Valor Minimo ao Valor Maximo
print(random.uniform(4, 10))
# Gera um valor inteiro de Valor ao Valor Maximo
print(random.randint(4, 10))

cores = ['verde','vermelho','azul']
#Escolher opção aleatoria
print(random.choices(cores, k=2))

cartas_de_um_baralho = ['carta1','carta2','carta3','carta4'] # Embaralhar uma Lista
print(random.shuffle(cartas_de_um_baralho))
print(cartas_de_um_baralho)


         
