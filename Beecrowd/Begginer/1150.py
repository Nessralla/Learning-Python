x = int(input())

while True:
    z = int(input())
    if z > x:
        break

count = 0
sum = 0
while sum <= z:
    sum += x
    x += 1
    count += 1

print(count)
