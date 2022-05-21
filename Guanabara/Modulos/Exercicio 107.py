from UtilidadesCeV import moeda

preço = float(input("Digite o valor que deseja calcular: "))
print(f"A metade de {preço} é {moeda.metade(preço)}")
print(f"O dobro de {preço} é {moeda.dobra(preço)}")
print(f"O valor {preço} aumentado em 10% é {moeda.aumentar(preço,10):.2f}")
print(F"O valor {preço} reduzido em 15% é {moeda.reduzir(preço,15):.2f}")