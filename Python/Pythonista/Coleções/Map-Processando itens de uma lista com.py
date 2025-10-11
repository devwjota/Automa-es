# Como podemos criar listas ?

# Criar listas usando Loops e Range()
numeros = []
for n in range(5):
    numeros.append(n)
print(numeros)

# Map
alunos = ['Larissa','Rafael','Marcus','John']
def aprovar_pessoa(nome):
    # Logica mas complexa
    return nome + 'APROVADO'
print(list(map(aprovar_pessoa, alunos)))





# nomes = ['Larissa','Rafael','Marcus','John']
# def pessoa_aprovada(pessoa):
#     if pessoa == 'Rafael':
#         return True
#     else:
#         return False