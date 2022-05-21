# faça um programa com uma lista chamada numeros. duas funções a sorteia(sorteia 5 numeros e coloca na lista)
# a função somapar vai somar os pares depois que os 5 numeros forem colocar na lista

from random import randint

numeros=list()


def sorteia(n):
    for i in range(n):
        numeros.append(randint(1,10))
    print(numeros)

def somapares(lista):
    soma = 0
    for i in range(len(numeros)):
        if numeros[i]%2==0:
            soma +=numeros[i]
    print(f"A soma dos numeros pares é {soma} ")

sorteia(5)
somapares(numeros)



