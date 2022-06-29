a = 1
b = 1
sum = 0


while True:
    sum += (a/b)
    a += 2
    b *= 2
    if a==39:
        break
print(f"{sum:.2f}")