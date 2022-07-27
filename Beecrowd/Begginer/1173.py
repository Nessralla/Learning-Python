num = int(input())

arr = [num]

for i in range(9):
    num *= 2
    arr.append(num)

for k,v in enumerate(arr):
    print(f"N[{k}] = {v}")
