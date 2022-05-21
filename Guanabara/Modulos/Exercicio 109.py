from UtilidadesCeV import moeda

preço = float(input("Digite o valor que deseja calcular: "))
perc1 = int(input("Digite a percentagem de aumento: "))
perc2 = int(input("Digite a percentagem de redução: "))
preçof = moeda.moeda(preço)
print("-="*20)
print(" "*7,"RESUMO"," "*7)
print("-="*20)
moeda.resumo(preço,perc1,perc2,True)
