arr=[]

for i in range(100):
    arr.append(float(input()))

for k,v in enumerate(arr):
    if v <= 10:
        print(f"A[{k}] = {v:.1f}")