# Crie um programa onde o usuário pode digitar 5 valores números para adicionar numa lista, já na posição 
# correta na lista. Sem usar o metodo sorted

lista = []

opc = int(input("Digite um número: "))
lista.append(opc)
print(f"Número {opc} adicionado com sucesso!")
opc = int(input("Digite um número: "))

if opc>=lista[0]:
    lista.append(opc)
    print(f"Número {opc} adicionado no final da lista")
else:
    lista.insert(0,opc)
    print(f"Número {opc} adiciona a lista na posição {lista.index(opc)}")

opc = int(input("Digite outro número: "))

if opc>=lista[1]:
    lista.append(opc)
    print(f"Número {opc} adiciona a lista na posição {lista.index(opc)}")
elif opc>=lista[0]:
    lista.insert(1,opc)
    print(f"Número {opc} adiciona a lista na posição {lista.index(opc)}")
else:
    lista.insert(0,opc)
    print(f"Número {opc} adiciona a lista na posição {lista.index(opc)}")

opc = int(input("Digite outro número: "))

if opc>=lista[2]:
    lista.append(opc)
    print(f"Número {opc} adiciona a lista na posição {lista.index(opc)}")
elif opc>=lista[1]:
    lista.insert(2,opc)
    print(f"Número {opc} adiciona a lista na posição {lista.index(opc)}")
elif opc>=lista[0]:
    lista.insert(1,opc)
    print(f"Número {opc} adiciona a lista na posição {lista.index(opc)}")
else:
    lista.insert(0,opc)
    print(f"Número {opc} adiciona a lista na posição {lista.index(opc)}")

opc = int(input("Digite outro número: "))

if opc>=lista[3]:
    lista.append(opc)
    print(f"Número {opc} adiciona a lista na posição {lista.index(opc)}")
elif opc>=lista[2]:
    lista.insert(3,opc)
    print(f"Número {opc} adiciona a lista na posição {lista.index(opc)}")
elif opc>=lista[1]:
    lista.insert(2,opc)
    print(f"Número {opc} adiciona a lista na posição {lista.index(opc)}")
elif opc>=lista[0]:
    lista.insert(1,opc)
    print(f"Número {opc} adiciona a lista na posição {lista.index(opc)}")
else:
    lista.insert(0,opc)
    print(f"Número {opc} adiciona a lista na posição {lista.index(opc)}")

print(lista)

#solução Guanabara
# lista = [] 
# for c in range(5):
#   n = int(input("Digite um número: "))
#   if c == 0 or n>lista[-1]        'SE o for o primeiro número digitado (c==0) ou se o numero digita(n) for maior do que o último numero da lista
#       lista.append(n)             'Adiciona o número digitado no final
#   else:
#       pos = 0                     'Variável para verificar a posição do número
#       while pos < len(lista)      'Enquanto a variável pos for menor do que o tamanho da lista
#           if n <= lista[pos]      'Se o número digitado (n) for menor do que o número na posição (pos) da lista
#               lista.insert(pos,n) 'Insere o número digitado (n) antes da posição (pos)
#               break
#           pos +=1                 'Incrementa 1 na variável contadora de posição