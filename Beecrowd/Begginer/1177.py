num = int(input())

arr=[]

for i in range(0,1000,3):
    for j in range(num):
        if i+j < 1000:
            arr.append(j)

for k,v in enumerate(arr):
    print(f"N[{k}] = {v}")