# print the amount of number from 0 to n that is between 10 and 20

n = int(input())

dentro = 0
fora = 0

for i in range(0,n):
    a = int(input())
    if 10 <= a <= 20:
        dentro += 1
    else:
        fora += 1

print(f"{dentro} in")
print(f"{fora} out")