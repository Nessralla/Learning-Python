# Print the sum of all odd numbers between start and end

start = int(input())

end = int(input())

soma = 0

step = 1

if end < start:
    step = -1

if end == start:
    soma = 0
else:
    for i in range(start-1,end,step):
        if i % 2 != 0:
            soma += i

print(soma)
