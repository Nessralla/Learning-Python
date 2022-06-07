while (True):
    a,b = list(map(int,input().split()))
    if a<=0 or b<=0:
        break
    if a > b:
        a,b = b,a
   
    lista = range(a,b+1)

    for i in lista:
        print(i, end=" ")

    print(f"Sum={sum(lista)}")