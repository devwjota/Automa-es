import json

usuarios_json="""{
    "name":"John Smith",
    "age": 30,
    "city":"New York",
    "isStudent":true,
    "gpa":3.5
}"""


# Salvar um string Json -> Arquivo Json
with open('desafio.json','w',encoding='utf-8') as arquivo_json:
    json.dump(usuarios_json,arquivo_json)