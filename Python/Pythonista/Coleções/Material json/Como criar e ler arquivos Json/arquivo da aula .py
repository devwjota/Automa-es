import json

# Criar ou ler Json existente
computador_json ="""{
    "marca": "Dell",
    "preço": 15000
}"""
# Lendo um strin Json 
data = json.loads(computador_json) #loads
print(data["preço"])
# Salvar um string Json - > Arquivo Json
with open('computador.json','w',encoding='utf-8') as arquivo_json:
    json.dump(computador_json,arquivo_json)
# Para ler um arquivo Json
with open('computador.json',encoding='utf-8') as arquivo_json:
    string_computador_json = json.load(arquivo_json) # convertendo Json -> String
    dicionario_computador_json = json.loads(string_computador_json) # Converter  de String -> Dicionario Python
    print(dicionario_computador_json["marca"])
