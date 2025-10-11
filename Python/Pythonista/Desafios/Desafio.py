# Desafio 🥇
possui_passaporte = False
passagem_comprada = False
menor_de_idade = False

# Uma pessoa só pode viajar se possuir  passaporte e tiver a passagem comprada e não for menor de idade
print(possui_passaporte == True and passagem_comprada and not menor_de_idade)
print((possui_passaporte and passagem_comprada) and not menor_de_idade) # professor

# Uma pessoa só pode viajar se possuir passaporte ou tiver a passagem comprada e não for menor de idade
print(possui_passaporte == True or passagem_comprada and not menor_de_idade)
print((possui_passaporte  or passagem_comprada) and not menor_de_idade) #professor


# Uma pessoa só pode viajar se não possuir passaporte ou tiver a passagem comprada e não for menor de idade
print(not possui_passaporte  or not passagem_comprada and menor_de_idade == False)
print((not possui_passaporte  or  passagem_comprada) and not menor_de_idade ) #professor

# Uma pessoa não pode viajar se não possuir passaporte ou não tiver a passagem comprada e for menor de idade
print (possui_passaporte == True or passagem_comprada and  menor_de_idade == False)
print ((not possui_passaporte or not passagem_comprada) and  menor_de_idade ) #professor
