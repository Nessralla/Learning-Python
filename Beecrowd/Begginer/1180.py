

arr = []

size = int(input())



arr = list(map(int,input().split()))

menor = min(arr)

print(f"Menor valor: {menor}")
print(f"Posicao: {arr.index(menor)}")



