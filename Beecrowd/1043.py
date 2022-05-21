A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)

if abs(B-C)<A<(B+C):
    if abs(A-C)<B<(A+C):
        if abs(A-B)<C<(A+B):
            print(f"Perimetro = {A+B+C}")
        else:
            print(f"Area = {((A+B)*C)/2}")
    else:
        print(f"Area = {((A+B)*C)/2}")
else:
    print(f"Area = {((A+B)*C)/2}")
