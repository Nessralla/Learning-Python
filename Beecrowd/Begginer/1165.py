def primo(num):
    for i in range(2,num):
        if num % i == 0:
            return f"{num} nao eh primo"
    return f"{num} eh primo"


size = int(input())

for i in range(size):
    num = int(input())
    print(primo(num))