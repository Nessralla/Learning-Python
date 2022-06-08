while True:
    a,b = list(map(int,input().split()))
    if a > b:
        print("Decrescente")
    elif a < b:
        print("Crescente")
    else:
        break