'''
Projeto - Medidor de Velocidade

Levando em consideração a velocidade maxima permitida de 80km em uma determinada rua. Crie um 
programa que recebe do usuario um valor que representa a velocidade e com base nessa velocidade 
diga se ela tomou uma multa leve ,grave,ou gravissima. Levando em consideração que se a pessoa
estiver abaixo da velocidade máxima seu programa deve exibir " não houve multa", caso esteja até
10km acima, deve exibir : "levou multa leve" caso esteja entre 11 a 20km acima da velocidade máxima,
exibir :" Levou multa grave", e caso esteja acima de 20km acima da velocidade máxima,exiba :" Levou multa gravíssima"

Analise criticamente o problema e descubra:
(Tente explicar este problema para voçe mesmo em voz alta e peça mais
informações/investigue mas ate voçe compreender completamente o problema.)


1. Quais são dados de entrada necessários ?
R: velocidade

2. O que devo fazer com estes dados ?
R: Criar um programa que recebe do usuario um valor que representa a velocidade , e com base nessa velocidade
dizer se ela tomou multa : leve , grave ou gravissima.

3. Quais são as restrições deste problema ?
R: se a pessoa
estiver abaixo da velocidade máxima seu programa deve exibir " não houve multa", caso esteja até
10km acima, deve exibir : "levou multa leve" caso esteja entre 11 a 20km acima da velocidade máxima,
exibir :" Levou multa grave", e caso esteja acima de 20km acima da velocidade máxima,exiba :" Levou multa gravíssima"


4. Qual é o resultado esperado ?
R: Criar um programa que recebe do usuario um valor que representa a velocidade e dizer se a multa foi leve,grave ou gravissima

5. Qual é  sequencia de passos a ser feitas para chegar ao resultado esperado ?

velocidade = input('Digite a sua Velocidade') # converter pra int
velocidade_maxima = 80

if velocidade <= velocidade_maxima:
    print 'Nao levou multa'

if velocidade > velocidade_maxima e velocidade <= velocidade_maxima + 10:
    print ' Levou multa leve'

if velocidade >= velocidade_maxima + 11 velocidade <= velocidade_maxima + 20:
    print ' Levou multa grave'

if velocidade  > velocidade_maxima + 20:
    print ' Levou multa gravissima'


'''
velocidade = int(input('Digite a sua Velocidade: '))
velocidade_maxima = 80

if velocidade <= velocidade_maxima:
    print ('Não levou multa')

elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:  # and
    print (' Levou multa leve')

elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print (' Levou multa grave')

elif velocidade  > velocidade_maxima + 20:
    print (' Levou multa gravissima')
