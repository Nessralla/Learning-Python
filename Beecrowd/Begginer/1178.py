num = float(input())

arr=[num]

for i in range(1,100):
    arr.append(num/2)
    num /= 2

for k,v in enumerate(arr):
    print(f"N[{k}] = {v:.4f}")