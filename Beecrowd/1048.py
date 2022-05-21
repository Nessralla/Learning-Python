salAtual = float(input())
i = 0

if salAtual <= 400.00:
    i = 0.15
elif 400.01 <= salAtual <=800.00:
    i = 0.12
elif 800.01<= salAtual <=1200.00:
    i = 0.10
elif 1200.01<= salAtual <=2000.00:
    i = 0.07
else:
    i = 0.04

print(f"Novo salario: {salAtual*(1+i):.2f}")
print(f"Reajuste ganho: {salAtual*i:.2f}")
print(f"Em percentual: {i*100:.0f} %")