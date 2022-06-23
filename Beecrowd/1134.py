opc = 0
Alcool = Gasolina = Diesel = 0
while opc != 4:
    opc = int(input())
    if opc == 1:
        Alcool += 1
    elif opc == 2:
        Gasolina += 1
    elif opc == 3:
        Diesel += 1
    elif opc == 4:
        break
    else:
        continue
print("MUITO OBRIGADO")
print(f"Alcool: {Alcool}")
print(f"Gasolina: {Gasolina}")
print(f"Diesel: {Diesel}")