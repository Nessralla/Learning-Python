expressao = input("Digite a expressão: ")
lista = []
for i in expressao:
    if i == "(":
        lista.append("(")
    elif i == ")":
        if len(lista)>0:
            lista.pop()
        else:
            lista.append(")")
            break

if len(lista) == 0:
    print("A expressão é válida")
else:
    print("A expressão é inválida")
