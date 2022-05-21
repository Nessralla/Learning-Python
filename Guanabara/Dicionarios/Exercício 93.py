# crie um programa que irá ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade
# de gols em cada partida. Ao final tudo deve ser guardado em um dicionário, incluindo o total de gols feio

relacao = {}

relacao["nome"] = input("Digite o nome do jogador: ")

relacao["partidas"] = int(input(f"Digite quantas partidas {relacao['nome']} jogou: "))

relacao['gols'] = []

for i in range(0,relacao['partidas']):
    
    relacao['gols'].append(int(input(f"Digite quantos gols foram feitos na partida {i+1}: ")))

print("-="*20)
print(relacao)
print("-="*20)
print(f"O campo valor nome tem o valor {relacao['nome']}")
print(f"O campo partidas tem o valor {relacao['partidas']}")
print(f"O campo gols tem o valor {relacao['gols']}")
print('-='*20)
print(f"O jogador {relacao['nome']} jogou {relacao['partidas']} partidas")
for i in range(0,relacao['partidas']):
    print(f"Na partida {i+1} ele fez {relacao['gols'][i]} gols")
print(f"Ele fez um total de {sum(relacao['gols'])}")