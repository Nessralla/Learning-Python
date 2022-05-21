a,b,c = input().split()
lista = []
a = float(a)
b = float(b)
c = float(c)

lista.append(a)
lista.append(b)
lista.append(c)

lista.sort(key=float)

a = lista[2]
b = lista[1]
c = lista[0]

if a>=b+c:
    print("NAO FORMA TRIANGULO")
else:
    if a**2==b**2+c**2:
        print("TRIANGULO RETANGULO")
    if a**2>b**2+c**2:
        print("TRIANGULO OBTUSANGULO")
    if a**2<b**2+c**2:
        print("TRIANGULO ACUTANGULO")
    if a==b==c:
        print("TRIANGULO EQUILATERO")
    if a==b!=c or a==c!=b or c==b!=a:
        print("TRIANGULO ISOSCELES")