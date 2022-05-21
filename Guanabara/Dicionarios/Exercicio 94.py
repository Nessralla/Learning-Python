# faça um programa que leia nome, sexo e idade de várias pessoas, guardando cada uma em um dicionario. 
# guarde os dicionários numa lista. após o fim da inserção de nomes, mostre quantas pessoas foram cadastradas 
# a media de idade do grupo, uma lista com as mulheres e uma lista com as idades acima da média

pessoas = []
cadastro = {}
idades = 0
opc = ''
media = 0

while True:
    cadastro['nome'] = input("Digite o nome da pessoa: ")
    cadastro['sexo'] = input("Digite M para masculino ou F para feminino: ").upper()
    while cadastro['sexo'] not in "MF":
        cadastro['sexo'] = input("Digite somente opções válidas!!! \n [M] para masculino ou [F] para feminino! \n").upper()
        if cadastro['sexo'] in "MF":
            break
    cadastro['idade'] = int(input("Digite a idade da pessoa: "))
    idades += cadastro['idade']
    pessoas.append(cadastro.copy())
    cadastro.clear()
    opc = input('Quer continuar? [S] ou [N]: ')
    while opc not in "NnSs":
        opc = input("Digite somente opções válidas!!! \n [S] para continuar ou [N] para encerrar! \n")
        if opc in "NnSs":
            break
    if opc in "Nn":
        break
    elif opc in "Ss":
        continue
        

print(pessoas)
print("-="*20)
print(f"Foram cadastradas {len(pessoas)} pessoas")
media = idades/len(pessoas)
print("-="*20)
print(f"A media de idade é {media} anos")
print("-="*20)
print("As mulheres cadastradas são: ")
for i in range(len(pessoas)):
    if pessoas[i]['sexo'] == "F":
        print(f"{pessoas[i]['nome']}...",end='')
print("\n"," -="*20)
print("\n As pessoas com idades acima da média são: ")
for i in range(len(pessoas)):
    if pessoas[i]['idade'] >= media:
        print(pessoas[i])
