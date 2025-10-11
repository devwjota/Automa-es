# Filter 

# Exemplo 1
nomes = ['Larissa','Rafael','Marcus','John']
def pessoa_aprovada(pessoa):
    if pessoa == 'Rafael':
        return True
    else:
        return False
    
print(list(filter(pessoa_aprovada, nomes))) # Exibe apenas o parametro
print(list(map(pessoa_aprovada, nomes))) # Mostra Qual e True e False no Caso 'Rafael' e True o resto False

# Exemplo 2
pinturas = [
    ['Pintura Classica','Azul',1857],
    ['Pintura Classica','Vermelha',1867],
    ['Pintura Classica','Verde',1897]
]

def eh_antiguidade(pintura):
    if pintura[2] < 1890:
        return True
    else:
        return False    

print(list(filter(eh_antiguidade, pinturas))) # Todas pinturas que for menor que 1890 
print(list(map(eh_antiguidade, pinturas)))  # O True e 1857 e 1867

# Desafio 🥇: Usando a lista abaixo, filtre apenas as vagas com salário acima de R$2500

vagas = [

    ['vaga 1', 1200],

    ['vaga 2', 2550],

    ['vaga 3', 5000]

]     

def vagas_emprego(vaga):
    if vaga[1] > 2500:
        return True
    else:
        return False
    
print(list(filter(vagas_emprego, vagas)))