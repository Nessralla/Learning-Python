sum = 0
NotasValidas = 2
opc = 1
sair = 0

while NotasValidas != 0:
        nota = float(input())
        if 0 <= nota <= 10:
            NotasValidas -= 1
            sum += nota
        else:
            print("nota invalida")
        if NotasValidas == 0:
            break

print(f"media = {sum/2:.2f}")


