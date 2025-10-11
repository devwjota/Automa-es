# Desafio - Transforme o codigo abaixo em uma função
velocidade = int(input('Digite sua velocidade:  '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print('Nao levou multa')

elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('Levou multa leve')

elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('Levou multa grave')

elif velocidade > velocidade_maxima + 20:
    print('Levou multa gravissima')
    
# Com Função
def multa_por_velocidade (velocidade,velocidade_maxima):
 if velocidade <= velocidade_maxima:
    print('Nao levou multa')

 elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('Levou multa leve')

 elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('Levou multa grave')

 elif velocidade > velocidade_maxima + 20:
    print('Levou multa gravissima')

multa_por_velocidade(122,100)