# Condicionais usando if , elif e else
trabalho_terminado = True
if trabalho_terminado == True:
    print(" Bora dar uma saida!")
else:
    print('Não posso sair agora')

#Exemplo 2
numero_atrasos = 2
if numero_atrasos >= 3 :
    print('Va para a diretoria')
elif numero_atrasos == 2:
    print('Essa e sua segunda falta')
elif numero_atrasos == 1:
    print('Essa e sua primeira falta')
else:
    print('Pode entrar ')

# Exemplo 3
velocidade = 55
if velocidade <=50:
    print('Não foi multado')
# elif velocidade >= 51 and velocidade <= 60:
elif 51 <= velocidade <= 60:
    print('Levou multa de 2 pontos')
elif velocidade >= 61 and velocidade <= 75:
    print('Levou multa de 3 pontos')
else:
    print('Levou multa de 7 pontos') 


