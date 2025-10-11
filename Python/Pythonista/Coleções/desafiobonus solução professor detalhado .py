# Desafio Bonus exmplicação professor 

# A lista a seguir define as extensões dos tipos de arquivos de que deverão ser criados
type_arquivos = ['.jpg', '.txt', '.mp3', '.xlsx', '.docx']

# A variável a seguir irá armazenar quantos arquivos com cada extensão o usuário desejará criar
quantidade_arquivos = int(input('Informe quantos arquivos deseja criar: '))
qtd = 1

# O primeiro 'for' irá garantir a criação da quantidade de arquivos vazios informados pelo usuário, para cada extensão!
'''
    O segundo for irá garantir que para cada iteração do primeiro laço,
     seja criado um arquivo vazio com cada uma das extensões definadas na lista!
'''
for t in type_arquivos:
    nome_arquivo = f'desafio/arquivo{qtd}{t}'  # Caminho completo do arquivo
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        if qtd >= quantidade_arquivos:
            break
        qtd += 1
