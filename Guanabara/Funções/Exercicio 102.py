# Crie uma função fatorial, com dois parametros, o 1º é o valor a ser fatorado, o 2º é o parâmetro que exibe
# ou não exibe o cálculo do fatorial. Além disso deve ter a docstring explicando o funcionando.

from time import sleep

def fatorial(n,show=False):

    """-> Calcula o fatorial do número 'n': 
    n = valor a ser fatorado
    show (opcional) = mostrar o cálculo passo a passo
    return = resultado da fatoração de n"""

    fat = 1
    
    if show == True:
        for i in range(1,n+1):
            fat *=i
            sleep(0.5)
            if i == n:
                print(f"{i} = ",end="") 
            
            else:
                print(f"{i} x ",end="")
    else:
        for i in range(1,n+1):
            fat *=i
        
    sleep(0.5)
    return fat

print(fatorial(5,show=True))