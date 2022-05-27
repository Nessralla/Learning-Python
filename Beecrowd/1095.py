# Faça um programa que imprima uma sequencia i=1 +3... e j=60 -5..., terminando com j em 0.

j=60
i=1

print(f"I={i} J={j}")

while j>0:
    j -= 5
    i += 3
    print(f"I={i} J={j}")
