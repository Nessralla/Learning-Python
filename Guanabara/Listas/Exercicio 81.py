# Crie uma lista que vai recber diversos números pelo usuário. Mostre quantos números foram digitados, a lista de valores em ordem
# decrescente e se o valor 5 foi digitado e esta ou não na lista

# lista.append(int(input("Digite um valor: "))) 'Não precisa declarar variável para apensar numero a lista

from operator import invert


lista = []

while True:
    opc = int(input("Digite um número: "))
    lista.append(opc)
    print(f"Número {opc} adicionado com sucesso!\n")
    opc = input("Deseja digitar mais um número? S para sim ou N para não\n")
    if opc in "Ss":
        continue
    else:
        break

print(f"Foram digitados {len(lista)} números \n")
print(sorted(lista,reverse=True))
if 5 in lista:
    print(f"O número 5 esta na lista na posição {lista.index(5)}")
else:
    print("O número 5 não foi digitado")
