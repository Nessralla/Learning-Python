lista = []
pos = 0
opc = ""
while True:
    lista.append(list())
    lista[pos].append(input("Digite o nome do aluno: "))
    lista[pos].append(list())
    lista[pos][1].append(float(input("Digite a primeira nota: ")))
    lista[pos][1].append(float(input("Digite a segunda nota: ")))
    lista[pos].append((lista[pos][1][0]+lista[pos][1][1])/2)
    opc = input("Deseja cadastrar mais um aluno? [S] para sim ou [N] para não \n")
    if opc in "Ss":
        pos +=1
        continue
    else:
        break
print("-="*15)
print("Num.     Nome        Média")
print("-"*30)
for i in range(len(lista)):
    print(f"{i+1:<8}{lista[i][0]:^8}{lista[1][2]:>8}")

while True:
    opc = int(input("Digite o número do aluno para ver as notas: 999 interrompe o programa: "))
    if opc == 999:
        print("Finalizando...")
        break
    else:
        print(f"As notas do aluno {lista[opc-1][0]} são {lista[opc-1][1][0]} e {lista[opc-1][1][1]}")