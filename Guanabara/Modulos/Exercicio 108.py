from UtilidadesCeV import moeda


preço = float(input("Digite o valor que deseja calcular: "))
preçof = moeda.moeda(preço)
print(f"A metade de {preçof} é {moeda.moeda(moeda.metade(preço))}")
print(f"O dobro de {preçof} é {moeda.moeda(moeda.dobra(preço))}")
print(f"O valor {preçof} aumentado em 10% é {moeda.moeda(moeda.aumentar(preço,10))}")
print(F"O valor {preçof} reduzido em 15% é {moeda.moeda(moeda.reduzir(preço,15))}")