start = int(input())
end = int(input())

if start > end:
  start,end = end,start

sum = 0

for i in range(start,end+1):
    if i % 13 == 0:
        continue
    else:
        sum += i
print(sum)