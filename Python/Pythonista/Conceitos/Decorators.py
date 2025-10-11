# Aproveitando e estendendo o que já está pronto

# Desafio 1
# Crie um decorador que ira pegar a função e for passado Para ele imprimir  o horário atual
# Antes de executar a função e depois imprimir O horário aposta é finalizado a execução da função

# Usando modulo datetime

# Importa datetime
from datetime import datetime
# Crie um decorador
def meu_horario(função):
    def emprego():
         print(datetime.now()) 
         função()
         print(datetime.now()) 
    return emprego

@meu_horario
def inicio_de_serviço():
    print('Inicio de Serviço')
inicio_de_serviço()

def fim_de_serviço():
    print('Serviço concluido com Sucesso')
fim_de_serviço()









    



