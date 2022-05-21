# Crie um programa onde 4 jpgadores joguem um dado, guarde os resultados em um dicionário
# Ao final coloque o dicionário em ordem

from random import randint
from time import sleep

relordenada = []
relacao = []
jogador = dict()
print("Iniciando o jogo")
sleep(0.5)
for i in range(4):
    jogador["nome"] = f"Jogador {i+1}"
    jogador["dado"] = randint(1,6)
    sleep(0.5)
    print(f"O {jogador['nome']} tirou {jogador['dado']}")
    if len(relacao) ==0:
        relacao.append(jogador.copy())
    else:
        for l in range(len(relacao),0,-1):
            if jogador["dado"] >= relacao[l-1]["dado"]:
                relacao.append(jogador.copy())
                break
            elif jogador["dado"]>= relacao[l-2]["dado"]:
                relacao.insert(l-1,jogador.copy())
                break
            else:
                relacao.insert(l-2,jogador.copy())
                break

    jogador.clear()

sleep(0.5)
print("-="*20)
print("Relação dos vencedores: ")
print(relacao)
for i in range(4,0,-1):
   print(f"O jogador {relacao[i-1]['nome']} tirou o valor {relacao[i-1]['dado']}")
   sleep(0.5)

# guanabara utilizou item getter from operator import itemgetter com sorted para fazer a lista de vencedor