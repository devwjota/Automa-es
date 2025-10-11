# 🥇 DESAFIO Manipulação de Arquivos🥇
'''
Veja o desafio, tente fazer por conta própria e depois veja a solução que estou passando aqui
# Primeiro crie 3 listas
 * Uma lista que contem 5 frutas
 * Uma lista que contem 5 cores
 * Uma lista que contem 5 linguagens de programação

 """
Como criar e modificar arquivos:
'w' -> Usado somente para escrever algo
'a' -> Usado para acrescentar algo
'r' -> Usado somente para ler algo
'r+'-> Usado para ler e escrever algo
"""

# Desafio 1 - Crie um novo arquivo chamado frutas.txt e insira dentro dele todos as 5 frutas que estão na lista de frutas
# Desafio 2 - Imprima na tela todas as linhas que estao dentro do arquivo frutas.txt
# Desafio 3 - Sem apagar os dados que já estão dentro de frutas.txt, adicione todas as cores que estão dentro da sua lista de cores ao arquivos frutas.txt
# Desafio 4 - Crie um novo arquivo chamado 'Top 5 Linguagens.txt' e popule o arquivo, de forma com que cada linuguagem ocupe apenas uma linha.
# BONUS - Como você poderia criar vários arquivos diferentes usando um laço for e strings dinâmicos(f'{}'), e também não escrever nada dentro deles?
'''
import os

frutas = ['Maçã','Banana','Pera','Uva','Tangerina']
cores  = ['Vermelho','Amarelo','Laranja','Roxo','Azul']
Linguagens = ['Python','Java','Html','Java Script','Php']

with open ('frutas.txt','w',encoding='utf-8') as arquivo:
    for fruta in frutas:
        arquivo.write(str(frutas) + (str(cores) + os.linesep))

with open ('Top 5 linguagens.txt','w') as arquivo:
    for lingua in Linguagens:
        arquivo.write(str(Linguagens) + os.linesep)
  


