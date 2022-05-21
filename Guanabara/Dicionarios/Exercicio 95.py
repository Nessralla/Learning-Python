# melhore o programa 93 para adicionar vários jogadores incluindo um sistema de visualização de aproveitamento

jogadores = []
cadastro = {}
opc = ""

while True:
    cadastro['nome'] = input("Digite o nome do jogador: ")
    cadastro['partidas'] = int(input("Digite quantas partidas ele jogou: "))
    cadastro['gols'] = list()
    for i in range(cadastro['partidas']):
        cadastro['gols'].append(int(input(f"Digite quantos gols {cadastro['nome']} fez na partida {i+1}: ")))
    jogadores.append(cadastro.copy())
    cadastro.clear
    opc = input("Quer continuar? [S] ou [N]: ")
    while opc not in "NnSs":
        opc = input("Digite somente opções válidas!!! \n [S] para continuar ou [N] para encerrar! \n")
    if opc in "Nn":
        break
    elif opc in "Ss":
        continue

opc = 0
print(jogadores)
print(jogadores[0]['gols'])

print("Cód  Nome        Gols                   Total")
for i in range(len(jogadores)):
    print(f"{i+1:<5}{jogadores[i]['nome']:^10} {jogadores[i]['gols']} {sum(jogadores[i]['gols']):>15}")
    # 

while True:
    opc = int(input("Digite o código do jogador que deseja ver todas as informações (999 sai): "))
    
    if opc == 999:
        break
    elif opc >= len(cadastro):
        print("Não existe nenhum jogador com este número de cadastro")
        continue
    else:
        print(f"\n Levantamento do jogador {jogadores[opc-1]['nome']}\n")
        for i in range(len(jogadores[opc-1]['gols'])):
            print(f" No jogo {i} ele fez {jogadores[opc-1]['gols'][i]}")
