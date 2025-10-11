# Exemplo 6 - Fatorial de um numero
"""
Crie um programa que receba um numero e imprima o fatorial daquele numero
# Método 5Q's para mostrar um algorítimo :

Analise criticamente o problema e descubra:
(Tente explicar este problema para voçe mesmo em voz alta e peça mais
informações/investigue mas ate voçe compreender completamente o problema.)


1. Quais são dados de entrada necessários ?
R: Número

2. O que devo fazer com estes dados ?
R: Calcular o fatorial do numero que for passado para o meu programa e exibir na tela 

3. Quais são as restrições deste problema ?
R:- O numero deve ser um valor positivo
- O numero deve ser um valor inteiro

4. Qual é o resultado esperado ?
R: O resultado esperado e que o fatorial do numero pedido seja exibido na tela.

5. Qual é  sequencia de passos a ser feitas para chegar ao resultado esperado ? R:
input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
    fatorial = fatorial * numero
print(fatorial)
"""
numero = int(input('Digite um número:'))
if numero > 0:
    fatorial = 1
    for item in range(1,numero + 1):
        fatorial = fatorial * item
    print(fatorial)
