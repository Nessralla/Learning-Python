lista = list(map(int,input().split()))

A = 0
N = 0
i = 0
sum = 0
while True:
    if lista[i] > 0:
        A = lista[i]
        N = lista[-1]
        break
    i += 1

for j in range(N):
    sum += A + j

print(sum)