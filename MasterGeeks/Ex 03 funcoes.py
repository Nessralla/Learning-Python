def test_valueError(n1, n2: int or float):

  while True:
    #n1 e n2 devem ser um nº seja ele float ou int.
    try:  
  
      #Mas se eles tiverem uma tipagem diferente da prevista.
      if type(n1) != int and type(n1) != float:
  
        #Voltamos a pegá-los como string para salvar o valor digitado.
        n1 = str(input('\nPor favor digite o 1º nº.\n'))
       
        #E depois tentamos a conversão para int ou float.
        n1 = float(n1)
        if n1%1 == 0:
          n1 = int(n1)   

  
        #Porque quando há um erro, o processo é interrompido e
        #os valores não são alterados. Ai não conseguimos mostrar
  
         #o que foi digitado incorretamente.
  
      if type(n2) != int and type(n2) != float:
        n2 = str(input('\nPor favor digite o 2º nº.\n'))
        n2 = float(n2)
        if n2%1 == 0:
          n2 = int(n2)
     
      break
  
    #Se o valor recebido não for convertido para int ou float,
    #teremos um ValueError.
    except ValueError:
      if type(n1) != int and type(n1) != float:
        print(f'\n{n1} não é um nº.')      
     
      else:
        print(f'\n{n2} não é um nº.')
       
  print(f'\n{n1} & {n2} são nº válidos.\n')
  
  


def test_ZeroDivisionError(num,den: int or float):
  while True:
    try:
      if den == 0:
        den = str(input("O denominador não pode ser 0. Por favor digite um novo número para o denominador:  "))
        den = float(den)
        if den%1 == 0:
          den = int(den)
      else:
        res = num/den
        print(f"O resultado da divisão de {num} por {den} é {res}")
        break
        
    except ZeroDivisionError:
      print(f"O número digitado foi {den}, não é possível dividir.")




def test_IndexError(ind,lista):
  while True:
    try:
        print(f"O número com índice {ind} é {lista[ind]}")
        break
    except IndexError:
        print(f"\nO índice {ind} esta fora da lista,por favor escolha somente índices entre 0 e {len(lista)-1}.\n")
        ind = int(input(f"\nDigite o índice desejado: \n"))

def test_Key_Error(k,dicio):

  while True:
    try:
      print(f"\nA chave {k} tem o item {dicio[k]}")
      break
    except KeyError:
      print("\nA chave digitada não existe no dicionário, favor digitar alguma das chaves abaixo: ")
      print(dicio.keys())
      k = input("\nNova chave: ")


def test_KeyboardInterrupt():
  while True:

    try:
      x = int(input("\nDigite um número"))
      break
    except KeyboardInterrupt:
      print("\nLarga de preguiça e digite o número manualmente")



# Criar a função KeyError

print('Teste 1º: n1 =  5  & n2 = 0'),      test_valueError(5, 0)
test_ZeroDivisionError(5, 0)
listaExemplo = [1,2,3,4,5,6,7]
test_IndexError(100,listaExemplo)
dicioExemplo = {'a':100,'b':50}
test_Key_Error('b',dicioExemplo)
test_KeyboardInterrupt()

  
#print('Teste 2º: n1 = "x" & n2 = 3'),      test_valueError('x', 3), test_ZeroDivisionError(5, 3)
  
#print('Teste 3º: n1 =  2  & n2 = "6,1"'),  test_valueError(2,'6,1')
