lista = [[],[]]

for i in range (7):
    opc = int(input("Digite um numero: "))
    if opc %2==0:
        lista[0].append(opc)
    else:
        lista[1].append(opc)

print(f"Os números pares são: {sorted(lista[0])} \n Os Numeros impares são: {sorted(lista[1])}")
