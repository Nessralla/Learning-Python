lista = list(map(int,input().split()))
step = lista[0]
end = lista[1]

i = 1

while i <= end:
    if i % step == 0:
        print(i) 
        i += 1
    else:
        print(f"{i}",end=" ")
        i += 1