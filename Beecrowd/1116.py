qtd = int(input())
res = 0


for i in range(qtd):
    x,y = list(map(int,input().split()))
    if y==0:
        print("divisao impossivel")
    else:
        res=x/y
        print(f"{res:.1f}")