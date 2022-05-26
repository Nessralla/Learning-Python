# Para cada N valores inputs, diga se são impares ou pares, e positivos ou negativos

qtd = int(input())

for i in range (qtd):
    numero = int(input())
    if numero == 0:
        print("NULL")
    elif numero > 0:
        if numero % 2 == 0:
            print("EVEN POSITIVE")
        else:
            print("ODD POSITIVE")
    else:
        if numero % 2 == 0:
            print("EVEN NEGATIVE")
        else:
            print("ODD NEGATIVE")