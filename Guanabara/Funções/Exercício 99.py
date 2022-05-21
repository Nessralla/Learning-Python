#o programa vai receber vários parâmetros, a função deve retornar o maior valor

from time import sleep

def maior(*num):
    print("-="*20)
    sleep(1)
    print("Analisando os valores passados: ")
    sleep(0.5)
    if len(num)==0:
        print(f"Foram passados {len(num)} valores ao todo")
        sleep(1)
        print(f"O maior valor encontrado foi 0")
        sleep(1)
    else:
        for n in num:
            print(f"{n}...",end='')
            sleep(0.5)
        print(f"\nForam passados {len(num)} valores ao todo")
        sleep(1)
        print(f"O maior valor encontrado foi {max(num)}")
        sleep(1)
    
    
    


maior(1,5,8,7,3,5,71,2,5,34,8,0,3,2,32,4,3,7)
maior(1,2,3,4,5)
maior(9,8,7,6)
maior()
