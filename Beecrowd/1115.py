while True:
    x,y = list(map(int,input().split()))
    if x>0 and y>0:
        print("primeiro")
        continue
    if x> 0 and y<0:
        print("quarto")
        continue
    if x<0 and y>0:
        print("segundo")
        continue
    if x<0 and y<0:
        print("terceiro")
        continue
    if x==0 or y==0:
        break