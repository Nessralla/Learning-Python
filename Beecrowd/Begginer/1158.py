n = int(input())

sum = 0
count = 0

for i in range(n):
    lst = list(map(int,input().split()))
    start = lst[0]
    end = lst[1]
    while count != end:
        if start%2!=0:
            sum += start
            count += 1
        start += 1
    print(sum)
    sum = 0
    count = 0