# Exercício para criar uma lista que recebe 5 números do usuário, verifica o maior e o menor, retornando
# as posições que eles aparecem


lista = []
a = ""
b = ""
c = ""

for i in range(5):
    lista.append(int(input("Digite um valor: ")))

if lista.count(max(lista)) > 1:
   
    
    for i in range(lista.count(max(lista))):
        c = str(lista.index(max(lista),lista.index(max(lista))+i))
        a += ("..."+c)
else:
    a = lista.index(max(lista))

if lista.count(min(lista)) > 1:
    
    for i in range(lista.count(min(lista))):
        c = str(lista.index(min(lista),lista.index(min(lista))+i))
        b += ("..."+c)
else:
    b = lista.index(min(lista))



print(f"Voce digitou os valores {lista}")
print(f"O maior valor digitado foi {max(lista)} na posição {a}")
print(f"O menor valor digitado foi {min(lista)} na posição {b}")