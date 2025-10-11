def somar (*valores, b):
    print(valores)
    for valor in valores:
        b+= valor
    print(b)

somar(50,60,5, b=12)
# *args

# Kwargs
# ** Kwargs (Keyword arguments)
def concatenar(**palavras):
    frase= ''
    for palavra in palavras.values():
        frase += palavra + ' '
    print(frase)

concatenar (a='Grandes',b='São',c='os',d='outros',e='o',f='Fluminense',g='e',h='Enorme')

# Exemplo 
def fazer_calculo (nome,*args,**kwargs):
    print(nome)
    print(args)
    print(kwargs)
    for arg in args:
        print(arg)
    for kwarg in kwargs.values():
        print(kwarg)
fazer_calculo('Wanderson',4,5,24,3,a=2,b=5,c=7)
