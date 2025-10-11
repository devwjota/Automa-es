#Vamos pensar por exemplo no seguinte :
idade = 21
possui_convite = False
filho_do_dono = True
print((idade >= 21 )and(possui_convite == True)) 
print(idade >=21 or possui_convite == True)

# maior de 21 e possui convite ou seja filho do dono 
print((idade > 21 and possui_convite == True) or (filho_do_dono == True))

# Exemplo
maior_de_idade = True
possui_carteira_de_trabalho = True
esta_trabalhando_atualmente = True
possui_veiculo_proprio = False

# Voçe so pode trabalhar aqui se for maior de idade e possuir a carteira de trabalho
print (maior_de_idade == True and possui_carteira_de_trabalho == True)

# Queremos contratar pessoas que ainda não possuem um veiculo proprio , mas ja possuam uma carteira de trabalho
print(possui_carteira_de_trabalho == True and not possui_veiculo_proprio)







