size = int(input())

for i in range(1,size+1):
    for j in range(1,4):
        if j == 3:
            print(f"{i**j}")
        else:
            print(f"{i**j}",end=" ")