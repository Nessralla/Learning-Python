# Crie uma função que irá retornar ajuda sobre outras funções, retornando ao menu principal

def ajuda():
    a = ""
    print("-="*20)
    print("SISTEMA DE AJUDA EM PYTHON!")
    print("-="*20)
    while True:
        a = input("Digite a função ou biblioteca para ter ajuda: ")
        if a.upper() != "FIM":
            print("-="*20)
            print(f"Acessando o manual da função {a}")
            print("-="*20)
            help(a)
        else:
            print("FIM")
            break

ajuda()