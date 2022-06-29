# Sequencia de I e J, com I começando em 0, muda de tres em tres e J,1,2,3. A cada ciclo ambos recebem 0.2

i = 0

while i < 2:

    for j in range(1,4):
        if i % 1.00 == 0 or i > 1.81:
            print(f"I={i:.0f} J={j+i:.0f}")
        else:
            print(f"I={i:.1f} J={j+i:.1f}")
    i += 0.2
