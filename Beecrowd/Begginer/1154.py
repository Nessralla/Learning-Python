count = 0
sum = 0

while True:
    num = int(input())
    if num < 0:
        break
    else:
        sum += num
        count += 1
print(f"{sum/count:.2f}")