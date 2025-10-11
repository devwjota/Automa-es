# Projeto chute o número
"""
Escreva um programa que, ao iniciar gera um valor aleatório de 1 a 10 e permite que o usuario
chute um numero ate que o valor aleatorio gerado no inicio do programa seja chutado correntamente.

O programa deve informar se o chute foi acima , abaixo ou igual ao valor
aleatorio gerado do inicio do programa.

# Metodo 5Q'S para montar um algoritmo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para voçe mesmo em voz alta e peça mais
informações/investigue mas ate voçe compreender completamente o problema.)

1. Quais são dados de entrada necessários ?
R: - Valor aleatorio de 1 a 10
   - Chute do usuario

2. O que devo fazer com estes dados ?
R: - Eu devo comparar o chute do usuario com o valor aleatorio que foi gerado no inicio do programa e
dizer se o chute foi maior > , menor < ou igual = ao valor que foi gerado no inicio do programa.

3. Quais são as restrições deste problema ?
R: Um valor aleatorio de 1 a 10

4. Qual é o resultado esperado ?
R: O resultado esperado deve informar se o chute foi acima , abaixo ou igual ao valor
aleatorio gerado do inicio do programa.


5. Qual é  sequencia de passos a ser feitas para chegar ao resultado esperado ?

input valor_aleatorio de 1 a 10
input chute
if chute > valor_aleatorio:
    print " Chute foi maior que o valor gerado"
if chute < valor_aleatorio
    print "Chute foi menor que o valor gerado"
if chute = valor_aleatorio
    print "Voçe acertou"
"""
import random

valor_aleatorio = random.randint(1,10) # gerando um valor aleatorio de 1 a 10
acertou = False

while acertou == False: # laço de repetição while 
    chute = int(input('Chute um valor de 1 a 10:  '))
    if chute > valor_aleatorio:
        print('Chute foi maior que o valor gerado:  ')
    elif chute < valor_aleatorio:
        print('Chute foi menor que o valor gerado:  ')
    elif chute == valor_aleatorio:
        acertou = True
        print('Voçe acertou!')














