# Tentativas 
tentativas = 0
while tentativas <3:
    print('tente novamente')
    tentativas += 1

# Senha
senha = ''
while senha != 'fluminense2024':
    senha = input('Digite sua senha :')
print('Bem-vindo!')

# # Receber nome do usuario
nome = ''
while nome == '':
    nome = input('Digite seu nome :')
print(f'Bem-Vindo {nome}')

# Ver o por do sol as 17:00
horario = 0
while horario <= 17:
    print(horario)
    horario += 1
print('Hora de ir ver o por do sol')

# Contagem Regressiva
contador = 100
while contador >= 0 :
    print(contador)
    contador -= 1




#DESAFIOS🥇

#DESAFIO 1 - Crie um loop while que irá contar e imprimir no console de 1 até 120
contador = 0
while contador <= 120:
    print(contador)
    contador += 1


#DESAFIO 2 - Crie um loop while que irá continuamente pedir ao usuário a senha para entrada, e só irá permitir o programa continuar caso ele digite a senha 'secreto'
senha = ''
while senha != 'secreto':
    senha = input('Digite sua senha :')
print('Bem-vindo!')

#DESAFIO 3 - Crie um loop que conte e imprima na tela o valor em ordem descrescente  de 100 para 1
valor = 100
while valor >= 1:
    print(valor)
    valor -= 1