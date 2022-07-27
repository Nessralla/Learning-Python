arr = []

for i in range(20):
    arr.append(int(input()))

for i in range(10):
    temp = arr[i]
    arr[i] = arr[-i-1]
    arr[-i-1] = temp

for k,v in enumerate(arr):
    print(f"N[{k}] = {v}")