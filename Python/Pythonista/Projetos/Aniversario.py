# Desafio 
# Calcule quantos dias faltam ate o seu Aniversario

from datetime import datetime
print(datetime.now())

dia_do_meu_aniversario = datetime(2024, 11, 22)
print(dia_do_meu_aniversario)

dia_para_meu_aniversario = datetime.strptime(input('Quantos dias faltam pro meu aniversario ? :'),'%d/%m/%Y')
print(type(dia_para_meu_aniversario))

data_atual = datetime.now()
data = dia_para_meu_aniversario - data_atual
print(data.days)


# Resposta do Professor    Resultado 252 dias  feito no dia 14/03/2024

# from datetime import datetime
# aniversario = datetime(2024,11,22)
# dias_para_aniversario = aniversario - datetime.now()
# print(dias_para_aniversario)





