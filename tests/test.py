import json
import random as rd
"""
* Extrair do de json de cada pessoa:
    - nome
    - CPF
    - idade
* Adicionar aleatoriamente a cada pessoa:
    - Faixa
    - Id de uma alguma turma
"""
with open("tests/pessoas_raw.json", "r") as pessoas_raw_file:
    pessoas_raw = json.load(pessoas_raw_file)

pessoas = [
    dict(
        nome=pessoa["nome"],
        cpf=pessoa["cpf"],
        idade=pessoa["idade"],
        turma_id=rd.randint(1, 2),
        faixa=rd.randint(1, 8),
    )
    for pessoa in pessoas_raw
]

with open("tests/pessoas.json", "w", encoding="utf8") as pessoas_file:
    json.dump(pessoas, pessoas_file, ensure_ascii=False)
