somaPositivos = 0
contPositivos = 0

for i in range(6):
    x = float(input())
    if x > 0:
        contPositivos += 1
        somaPositivos += x

print(contPositivos, "valores positivos")
print(f"{(somaPositivos/contPositivos):.1f}")