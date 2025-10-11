
for numero in range(100):
    if numero % 2 == 0 :
        print(numero)
    else:
        continue # continue , ignorar/pular


for numero in range (100):
    if numero in range(100):
        print(numero)
    else:
        break   # break , para interronper a iteração


# Exemplo 'continue'
frutas = ['Maçã', 'Manga','Laranja','Morango']
for fruta in frutas:
    if fruta == 'Manga':
        continue
    print(f'{fruta} adicionada a dieta')   # O continue vai fazer que o codigo pule a variavel 'Manga'


frutas = ['Maçã', 'Manga','Laranja','Morango']
for fruta in frutas:
    if fruta == 'Manga':
        break
    print(f'{fruta} adicionada a dieta')  # Vai interromper ou seja para na variavel 'Manga'



# DESAFIOS 🥇

# Desafio 1
#Use a operação necessária(break ou continue) para que a seguinte condição aconteça.
# Ao chegar ao estilo "Rap" o mesmo não deve ser impresso na tela

estilos = ['Hip-Hop','Rock','Rap','Pop']
for estilo in estilos:
    if estilo =='Rap':
        continue
    print(f'{estilo}')


## Desafio 2 
#Use a operação necessária(braek ou continue) para que a seguinte condição aconteça:
# Ao chegar ao estilo "Rock" a execução deve interrompida
estilos = ['Hip-Hop','Rock','Rap','Pop']
for estilo in estilos:
    if estilo == 'Rap':
        break
    print(f'{estilo}')


