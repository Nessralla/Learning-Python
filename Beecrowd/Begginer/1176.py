arrFib = [0,1]

for i in range(2,61):
    arrFib.append(arrFib[i-1] + arrFib[i-2])

cases = int(input())

for i in range(cases):
    a = int(input())
    print(f"Fib({a}) = {arrFib[a]}")

