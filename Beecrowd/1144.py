size = int(input())

for i in range(1,size+1):
    for j in range(1,4):
        a = i**j
        if j == 3:
            print(f"{a}")
        else:
            print(f"{a}",end=" ")
    for k in range(1,4):
        a = i**k
        if k == 3:
            print(f"{a+1}")
        elif k == 2:
            print(f"{a+1}",end=" ")
        else:
            print(f"{a}",end=" ")
        
