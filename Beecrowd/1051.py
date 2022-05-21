sal = float(input())
resto = 0
taxes = 0

if sal <= 2000.00:
    print("Isento")
elif sal <=3000.00:
    resto = sal - 2000
    taxes = resto*0.08
    print(f"R$ {taxes:.2f}")
elif sal <=4500.00:
    resto = sal - 3000
    taxes = resto*0.18 + 80
    print(f"R$ {taxes:.2f}")
else:
    resto = sal - 4500
    taxes = resto*0.28+80+270
    print(f"R$ {taxes:.2f}")