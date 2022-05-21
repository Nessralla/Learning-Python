# aprimirar o exercicio 86 - mostrar soma dos valores pares, a soma dos valores da terceira coluna, maior valor da segunda linha

lista = [[],[],[]]
pares = 0
terceiraColuna = 0

for c in range (3):
    for l in range (3):
        lista[c].append(int(input(f"Digite um numero na posição [{c}][{l}]: ")))
        if lista[c][l] %2==0:
            pares += lista[c][l]
        if l ==2:
            terceiraColuna += lista[c][l]


for c in range(3):
    for l in range(3):
        print ("[ ",lista[c][l]," ]",end="")
    print("\n")


print(f"A soma dos números pares é: {pares}")
print(f"A soma dos valores da terceira coluna é: {terceiraColuna}")
print(f"O maior valor da segunda linha é: {max(lista[1])}")