size = int(input())

for i in range(size):
    lst = list(map(float,input().split()))
    grA = lst[2]/100
    grB = lst[3]/100
    popA = int(lst[0])
    popB = int(lst[1])
    count = 0
    while True:
        count += 1
        if count ==101:
            print("Mais de 1 seculo.")
            break
        popA = int(popA*(1+grA))
        popB = int(popB*(1+grB))

        #print(f"Population A is: {popA} - Population B is: {popB}")
        if popA > popB:
            print(f"{count:.0f} anos.")
            break