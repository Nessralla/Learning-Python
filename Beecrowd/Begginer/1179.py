pares = []
impares = []

for i in range(15):
    num = int(input())
    if num%2==0:
        pares.append(num)
        if len(pares) == 5:
            for k,v in enumerate(pares):
                print(f"par[{k}] = {v}")
            pares.clear()
    else:
        impares.append(num)
        if len(impares)==5:
            for k,v in enumerate(impares):
                print(f"impar[{k}] = {v}")
            impares.clear()

for k,v in enumerate(impares):
    print(f"impar[{k}] = {v}")

for k,v in enumerate(pares):
    print(f"par[{k}] = {v}")
