from random import randint
from re import A
from time import sleep
jogos = []
a = 0

qtdJogos = int(input("Olá, Quantos jogos da MegaSena você quer fazer: "))
for j in range(qtdJogos):
    jogos.append(list())
    while len(jogos[j])<6:
        a = randint(1,60)
        if a not in jogos[j]:
            jogos[j].append(a)

print("-="*20)
for i in range(qtdJogos):
    print(f" Jogo {i+1:^3} : {sorted(jogos[i])}")
    sleep(2)