# Print 6 odd numbers from start

start = int(input())

count = 0

while count < 6:
    if start %2 != 0:
        print(start)
        count += 1
    start += 1