# Crie um programa que irá receber vários número do usuário. Após isso separe em outras duas listas os pares
# e os ímpares.

lista = []
pares = []
impares = []

while True:
    opc = int(input("Digite um número: "))
    lista.append(opc)
    print(f"Número {opc} adicionado com sucesso!\n")
    opc = input("Deseja digitar mais um número? S para sim ou N para não\n")
    if opc in "Ss":
        continue
    else:
        break

for i in lista:
    if i%2==0:
        pares.append(i)
    else:
        impares.append(i)

print(f"Os números digitados foram: {lista}")

print(f"Os números pares são: {pares}")

print(f"Os números ímpares são: {impares}")