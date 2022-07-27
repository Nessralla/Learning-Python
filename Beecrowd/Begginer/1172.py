arr = []

for i in range(10):
    a = int(input())
    if a <= 1:
        arr.append(1)
    else:
        arr.append(a)
    
for k,v in enumerate(arr):
    print(f"X[{k}] = {v}")


