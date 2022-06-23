size = int(input())

start = 1
end = 4
for i in range(size):
    for i in range(start,end):
        print(i, end = " ")
    print("PUM")
    start = end + 1
    end += 4