from turtle import Turtle

t = Turtle()

while True:
    direcao = input('Para qual direção devemos ir? "f:frente" ou "t:trás"')
    if direcao == 'f':
        distancia = int(
            input('Quantos pixels devemos movimentar para a frente?'))
        movimentar_para_lado = input(
            'Rotacionar para d:direta, e:esquerda n:não rotacionar')
        if movimentar_para_lado == 'd':
            angulo = int(input('Quanto para a direta devemos rotacionar?'))
            t.right(angulo)
        elif movimentar_para_lado == 'e':
            angulo = int(input('Quanto para a esquerda devemos rotacionar?'))
            t.left(angulo)
        t.forward(distancia)
    if direcao == 't':
        distancia = int(
            input('Quantos pixels devemos movimentar para a trás?'))
        movimentar_para_lado = input(
            'Rotacionar para d:direta, e:esquerda n:não rotacionar')
        if movimentar_para_lado == 'd':
            angulo = int(input('Quanto para a direta devemos rotacionar?'))
            t.right(angulo)
        elif movimentar_para_lado == 'e':
            angulo = int(input('Quanto para a esquerda devemos rotacionar?'))
            t.left(angulo)
        t.backward(distancia)
    resposta = input('Continuar andando?')
    if resposta not in ('sim', 's'):
        break

#  Clean code >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from turtle import Turtle
t = Turtle()

def obter_distancia():
    resposta=int(input('Quantos pixels devemos movimentar para a frente?'))
    return resposta

def rotacionar_turtle(Turtle):
    movimentar_para_lado =input('Rotacionar para d:direita e:esquerda n:não rotacionar')

    if movimentar_para_lado =='d':
        rotacionar_para_direita(Turtle)

    elif movimentar_para_lado =='e':
        rotacionar_para_esquerda(Turtle)

    def rotacionar_para_direita(Turtle):
        angulo = int(input('Quanto para a direita devemos rotacionar ? :'))
        t.right(angulo)

    def rotacionar_para_esquerda(Turtle):
        angulo = int(input('Quanto para esquerda devmos rotacionar ? :'))
        t.left(angulo)

    while True :
        direção = input('Para qual direção devemos ir ? "f:frente ou "t:tras" ')

        if direção == 'f':
            distancia = obter_distancia()
            rotacionar_turtle(t)
            t.forward(distancia)

        if direção =='t':
            distancia = obter_distancia()
            rotacionar_turtle(t)
            t.backward(distancia)

        resposta = input('Continuar andando ? :')
        if resposta not in ('sim','s'):
            break
        
               

