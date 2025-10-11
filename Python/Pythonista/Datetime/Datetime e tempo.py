from datetime import datetime
print(datetime.now().now) 
print(datetime.now().day)
print(datetime.now().month)
print(datetime.now().year)

# Criar uma data
Lançamento_app = datetime(2024, 6 , 21)
print(Lançamento_app)
# Quero receber a data Lançamento do meu app 
# 21/06/2024
data_de_lançamento = datetime.strptime(input('Quando devemos lançar o app ? :'), '%d/%m/%Y')
print(type(data_de_lançamento))

#Calcular o intervalo entre datas 
data_atual = datetime.now()
prazo = data_de_lançamento - data_atual
print(prazo.days)



