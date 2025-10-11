from datetime import datetime
import random

# Bem vindo a nossa empresa
print(' Bem vindo a nossa Empresa  ')

# Nome
nome = input('Digite seu Nome: ') #variavel = função ('string' )

# Idade
idade = int(input('Digite sua idade:')) #int : numero inteiro 

# data do cadastro
data_do_registro = datetime.now()

#cartões 
cartões = ['R$50,00','R$250,00','R$120,00']
cartão = random.choice(cartões)
#O método choice() retorna um elemento selecionado aleatoriamente da sequência especificada. A sequência pode ser uma string, um intervalo, uma lista, uma tupla ou qualquer outro tipo de sequência.

# data de aniversario
aniversario = datetime.strptime(
    input('Digite sua data de aniversario no formato dd/mm/aaaa: '), 
    '%d/%m/%Y')



# conclusão do registro
print(f' Ola {nome}, seu registro foi concluido com sucesso no dia{data_do_registro.day}/{data_do_registro.month}/{data_do_registro.year}.\nParabens, houve um sorteio e voçe ganhou um cartão de compras novalor de {cartão}')
      
















