# Faça um programa que receba uma função chaamda contador, com 3 parametros. (inicio, fim, step)
# 3 situações, de 1 a 10 de 1 em 1, de 10 a 0 de 2 em 2, e personalizado com varios testes abaixo:
# (5,-5,0) (20,80,10) (100,40,-20) etc

from time import sleep

def contagem(start,end,step):
    if step==0:
        step=1
    if step<0:
        step = -step

    if start<end:
        for i in range(start,end+1,step):
            print(f"{i}...",end="")
            sleep(0.5)
        print("FIM")

    elif start>end:
        for i in range(start,end-1,-step):
            print(f"{i}...",end="")
            sleep(0.5)
        print("FIM")

print("-="*20)
print("Contagem de 0 a 10 de 1 em 1: ")
contagem(0,10,1)
print("-="*20)
print("Contagem de 10 a 0 de 2 em 2: ")
contagem(10,0,2)
print("Agora é a sua vez de personalizar!")
sta = int(input("Digite o início da contagem: "))
en = int(input("Digite o final da contagem: "))
ste = int(input("Digite o passo da contagem: "))
contagem(sta,en,ste)
