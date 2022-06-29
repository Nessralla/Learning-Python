a,b = input().split()
a = int(a)
b = int(b)

x = (24 - a) + b

if x>24:
    x = b-a
    
print("O JOGO DUROU {} HORA(S)".format(x))