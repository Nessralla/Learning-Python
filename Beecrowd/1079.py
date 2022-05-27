# Para cada n casos, leia três valores e mostre a media ponderada

tCase = int(input())

for i in range (tCase):
    a,b,c= list(map(float, input().split()))
    print(f"{(a*2+b*3+c*5)/10:.1f}")
