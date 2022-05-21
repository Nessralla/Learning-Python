# Crie uma função chamada voto que com base na idade da pessoa, retorna se o voto é OBRIGATORIO, OPCIONAL OU NEGADO

def voto(x):
    if (2022-x)<16:
        return "PROIBIDO"
    elif (2022-x)>=60:
        return "OPCIONAL"
    else:
        return "OBRIGATORIO"

idade = int(input("Digite o ano que você nasceu: "))
print(f"Com {2022-idade} anos o voto é {voto(idade)}")