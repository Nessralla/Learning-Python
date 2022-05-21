# Faça um programa que leia o nome e o peso de várias pessoas e guarde numa lista
# Ao final mostre quantas pessoas foram cadastradas, uma listagem dos mais pesados e uma listagem dos mais leves

lista = []
listaCadastro = []
opc = ""

while True:
    listaCadastro.append(input("Digite um nome: "))
    listaCadastro.append(int(input("Digite o peso: ")))
    lista.append(listaCadastro[:])
    listaCadastro.clear()
    opc = input("Deseja cadastrar mais usuários? [S] ou [N]")
    if opc in "Ss":
        continue
    else:
        break

maior = lista[0][1]
menor = lista[0][1]

for i in range(len(lista)):
    if lista[i][1] >= maior:
        maior = lista[i][1]
    elif lista[i][1] <= menor:
        menor = lista[i][1]


print(f"\n Você cadastrou {len(lista)} pessoas \n")

print(f"O maior peso foi {maior} de ")
for i in range (len(lista)):
    if lista[i][1] == maior:
        print(f"{lista[i][0]}...",end="")

print(f"\n O menor peso foi {menor} de ")
for i in range (len(lista)):
    if lista[i][1] == menor:
        print(f"{lista[i][0]}...",end="")