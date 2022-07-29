sum = 0
NotasValidas = 2
opc = 1
sair = 0

while True:
    if opc == 2:
        break

 
    if opc == 1:
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
    NotasValidas = 2
    sum = 0
    opc = 0
    opc = int(input("novo calculo (1-sim 2-nao)\n"))