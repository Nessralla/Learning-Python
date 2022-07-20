def perfeito(num):
    soma = 0
    for i in range(1,num):
        if num % i == 0:
            soma += i
    return soma
            

cases = int(input())

for i in range(cases):
    num = int(input())
    if perfeito(num) == num:
        print(f"{num} eh perfeito")
    else:
        print(f"{num} nao eh perfeito")