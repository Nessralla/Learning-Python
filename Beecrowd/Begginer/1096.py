# Faça um programa que imprima uma sequencia i=1,i=1,i=1,i=3,i=3,i=3... até i=9,i=9,i=9
#  e j=7,j=6,j=5,j=7,etc.

for i in range(1,10,2):
    for j in range(7,4,-1):
        print(f"I={i} J={j}")