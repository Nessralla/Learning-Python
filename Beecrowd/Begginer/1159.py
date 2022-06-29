while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    sum = 0
    while count!=5:
        if n%2==0:
            sum +=  n
            count += 1
        n += 1

    print(sum)