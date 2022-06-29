start = int(input())
end = int(input())

if start > end:
  start,end = end,start

for i in range(start+1,end):
    if i%5==2 or i%5==3:
        print(i)