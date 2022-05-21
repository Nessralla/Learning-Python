# Crie um programa que leia nome, ano de nascimento, e carteira de trabalho e cadaste-os (com idade)
# se a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa irá se aposentar. Se aposenta com 35 anos de contribuição.


import enum
from datetime import datetime

pessoa = dict()
pessoa["nome"] = str(input("Digite seu nome: "))
#Guanabara utilizou a função datetime para pegar o ano atual
pessoa["nasc"] = datetime.now.year - int(input("Digite o ano de nascimento: "))
pessoa["CTPS"] = int(input("Digite seu número da carteira de trabalho. (0 para não tem): "))
if pessoa["CTPS"] == 0:
    print("Ok obrigado")
else:
    pessoa["contratacao"] = int(input("Digite o ano de sua primeira contratação: "))
    pessoa["salario"] = float(input("Digite seu salario: "))
    if 2022 - pessoa["contratacao"] >= 35:
        pessoa["aposenta"] = "Já pode se aposentar"
    else:
        pessoa["aposenta"] = f"Faltam {35-(2022-pessoa['contratacao'])} anos para se aposentar"

print(pessoa)
for i,(k,v) in enumerate(pessoa.items()):
    print(f"A chave {k} tem o valor {v}")
