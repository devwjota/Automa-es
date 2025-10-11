valores = [1,2,3,4,5,6,7,8,9,10]
anos = [2020, 2030, 2040, 2050]

# Adicionar ao final da lista
valores.append(11)
print(valores)

# Unir listas
valores.extend(anos)
print(valores)

# Adcionar lista  ' + '
nova_lista = valores + anos
print(nova_lista)

# Inserir  'insert'
print(anos[1])
anos.insert(2,2031)
print(anos)

# Extrair com base no indice 'pop'
anos_2020 = anos.pop(0)
print(anos_2020)

# Remover item da lista usando 'remove'
anos.remove(2050)
print(anos)

# # Ou pela função 'del' removendo pelo indice
del anos [3]
print(anos)

# Remover valor do 2 a 6 usando o 'del' a variavel e  os numeros que serão removidos[1:7]
del valores[1:7]
print(valores)

# Contando a ocorrencia de um valor usando a variavel .'count' (eo valor aqui))
print(valores.count(2))

# Resetar
valores.clear()
print(valores)


