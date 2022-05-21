# Crie uma função chamada leiaint(), que funcionará semelhante a função input, porém só aceita numeros inteiros.

def leiaInt(a):
    while True:
        x = input(a)
        try:
            int(x)
            break
        except:
            print("\n\033[0;31m Inválido, digite um número inteiro! \033[m \n")
    return x

n = leiaInt("Digite um numero: ")
print(f"\nVocê digitou o número {n}")