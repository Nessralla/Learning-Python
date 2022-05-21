lista = [[],[],[]]

for c in range (3):
    for l in range (3):
        lista[c].append(int(input(f"Digite um numero na posição [{c}][{l}]: ")))

for c in range(3):
    for l in range(3):
        print (f"[ {lista[c][l]:^5} ]",end="")
    print("\n")