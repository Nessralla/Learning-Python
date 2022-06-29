# Leia N casos, sendo que cada caso contém um numero (quantidade) e letra (animal). Ao final mostre o total de animais
# O total de cada tipo e também sua proporção

Coelho = 0
Rato = 0
Sapo = 0

tCase = int(input())
for i in range(tCase):
    a,b=input().split()
    a = int(a)
    if b == "C":
        Coelho += a
    elif b == "R":
        Rato += a
    else:
        Sapo += a

total = Coelho+Rato+Sapo

print(f"Total: {total} cobaias")
print(f"Total de coelhos: {Coelho}")
print(f"Total de ratos: {Rato}")
print(f"Total de sapos: {Sapo}")
print(f"Percentual de coelhos: {(Coelho/total)*100:.2f} %")
print(f"Percentual de ratos: {(Rato/total)*100:.2f} %")
print(f"Percentual de sapos: {(Sapo/total)*100:.2f} %")