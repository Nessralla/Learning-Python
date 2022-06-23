vInter = 0
vGremio = 0
empates = 0
opc = 1
lista = 0

while True:
    if opc == 2:
        break
    elif opc == 1:
        lista = list(map(int,input().split()))
        golsInter = lista[0]
        golsGremio = lista[1]
        if golsInter > golsGremio:
            vInter += 1
        elif golsGremio > golsInter:
            vGremio +=1
        else:
            empates += 1
        lista.clear()
        opc = int(input("Novo grenal (1-sim 2-nao)\n"))
print(f"{vInter+vGremio+empates} grenais")
print(f"Inter:{vInter}")
print(f"Gremio:{vGremio}")
print(f"Empates:{empates}")

if vInter > vGremio:
    print("Inter venceu mais")
elif vGremio > vInter:
    print("Gremio venceu mais")
else:
    print("Não houve vencedor")