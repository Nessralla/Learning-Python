# Faça um programa chamado ficha, com dois parametros opcionais, o nome do jogador e quantos gols ele marcou.
# Se não for passado o parâmetro nome do jogador, deve retornar <desconhecido>, se gols, retorna 0.

def ficha(n="<desconhecido>",g=0):
    return n,g

nome = input("Digite o nome do jogador: ")
gols = input("Digite quantos gols o jogador fez: ")

print(f"O jogador {ficha(nome,gols)[0]} fez {ficha(nome,gols)[1]} gols no campeonato")