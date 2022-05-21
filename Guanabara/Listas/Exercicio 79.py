#Criar um programa que recebe valores do usuário, insira numa lista, impeça de adicionar repetidos.
#Pergunte ao usuário se quer adicionar mais números ou não, se não, imprimir a lista dos números em ordem.

lista = []

while True:
    a = int(input("Digite um numero para ser adicionado a lista: "))
    if a not in lista:
        lista.append(a)
        opc = input("Número adicionado com sucesso. Deseja adicionar mais números? \n S para sim ou N para não: ")
        if opc in "Ss":
            continue
        else:
            print("\n Programa encerrado, abaixo listagem dos numeros")
            print(sorted(lista))
            break
    else:
        opc = input("Número não adicionado pois já estava na lista. Deseja continuar? \n S para sim ou N para não: ")
        if opc in "Ss":
            continue
        else:
            print("\n Programa encerrado, abaixo listagem dos numeros")
            print(sorted(lista))
            break
        