x,y,z = input().split()

x = int(x)
y = int(y)
z = int(z)

if x >= y:
    if y>= z:
        print(z)
        print(y)
        print(x)
    elif x>= z:
        print(y)
        print(z)
        print(x)
    else:
        print(y)
        print(x)
        print(z)
elif y>= x:
    if x>= z:
        print(z)
        print(x)
        print(y)
    elif y>= z:
        print(x)
        print(z)
        print(y)
    else:
        print(x)
        print(y)
        print(z)

print("")
print(x)
print(y)
print(z)