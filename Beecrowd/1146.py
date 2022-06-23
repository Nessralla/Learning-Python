while True:
    size = int(input())
    if size == 0:
        break
    else:
        for i in range(1,size+1):
            if i == size:
                print(i)
            else:
                print(f"{i}",end=" ")