# Condicionais
# if
# elif
# else

# Exemplo 1 :
"""
E ae Wanderson, bora dar  uma saida hoje ?
Se eu terminar meu trabalho aqui, eu consigo
"""
trabalho_terminado = True # Se colocar False vai cair pra condição else
if trabalho_terminado == True:
    print('Partiu, Bora sair !')
else:
    print('Não vai dar pra Sair agora .')

# Exemplo 2 :
"""
Ei, voçe consegue me ajudar a mover essas caixas la fora hoje a tarde ?
Se eu estiver livre, sim. Mas se não der pede meu irmão para te ajudar
"""
mover_caixas = True
if mover_caixas == True:
    print('Ajudo sim cara vamos la!')
else:
    print('Pede meu irmão para te ajudar.')

# Exemplo 3 :
"""
Eu cheguei atrasado na aula, ainda posso entrar?
Se essa não foi sua terceira vez chegando atrasado então pode sim ,
caso ao contrario ira tomar uma suspensão.
"""
numero_de_atrasos = 2
if numero_de_atrasos >= 3:
    print('Voçe esta suspenso!')
elif  numero_de_atrasos == 1:
    print('Pode entrar, porem caso tome mais 2 faltas, ira ser suspenso !')
elif numero_de_atrasos == 2:
    print('Pode entrar, porem caso tome mais 1 falta, ira ser suspenso !')
else:
    print('Pode entrar !')

# Exemplo 4 :
"""
input primeiro_valor
input segundo_valor
if primeiro_valor > segundo_valor
    print o primeiro valor e maior
else
    print o segundo valor e maior
     
"""
primeiro_valor = input('Digite o 1 valor:')
segundo_valor = input('Digite o 2 valor:')

if int(primeiro_valor) > int(segundo_valor):
    print('O primeiro valor e maior !')
else:
    print('O segundo valor e maior !')
