# Conversão entre tipo
idade = input('Digite a sua idade :')
print(int(idade)> 17)

ano_publicação = 2024
print('Este livro foi criado em'+ str(ano_publicação))

altura = input('Altura da parede? :')
print(float(altura)>2.50)

# Conversões entre coleções 
saudação = ' Hello! '
print(list(saudação))
print(set(saudação))
print(tuple(saudação))
print(list(range(30)))

numeros = [10,20,20,50]
print(set(numeros))
print(tuple(numeros))
print(type(numeros))
