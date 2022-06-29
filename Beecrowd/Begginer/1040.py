a,b,c,d = input().split()

a = float(a)
b = float(b)
c = float(c)
d = float(d)

media = (a*2+b*3+c*4+d*1)/10

print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.")
elif media <5.0:
    print("Aluno reprovado")
else:
    print("Aluno em exame.")
    x = float(input())
    print(f"Nota do exame: {x}")
    media = (media+x)/2
    if media >= 5.0:
        print("Aluno aprovado.")
        print(f"Media final: {media:.1f}")
    else:
        print("Aluno reprovado")
        print(f"Mediafinal: {media:.1f}")
