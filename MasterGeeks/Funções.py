#Obtém 2 números inteiros.
a = int(input('Digite o 1º número: \t')) #Obs. Assim como '\n' o comando '\t'
b = int(input('Digite o 2º número: \t')) #Também edita o texto.
                                        #Só que ao invés de pular linha, ele
                                        #Adiciona um espaço em branco de  
                                        #aproximadamente cinco caracteres.

#E depois exibimos a soma deles.
print(f'\nA soma desses dois números é: {a+b}')

#Quando o usuário quiser, ele pode apertar Enter ou qualquer outro botão
#para continuar a execução do programa.
input('\nAperte enter para continuar \n')

a = int(input('Digite o 3º número: \t'))
b = int(input('Digite o 4º número: \t'))

print(f'\nA multiplicação desses dois números é: {a*b}')

def continuar(): #<- Nossa 3º rotina, se transformou na função “Continuar”
 input('\nAperte enter para continuar \n')

a = int(input('Digite o 1º número: \t'))
b = int(input('Digite o 2º número: \t'))

print(f'\nA soma desses dois números é: {a+b}')

continuar() #<- E ao ser chamada, ela executa os comandos que estão dentro dela.


a = int(input('Digite o 3º número: \t'))
b = int(input('Digite o 4º número: \t'))

print(f'\nA multiplicação desses dois números é: {a*b}')

#criando a função hipotenusa

def medirHipotenusa():
 b = int(input("\nDigite um nº \n"))
 c = int(input("\nDigite um nº \n"))

 a = int(((b**2) + (c**2))**0.5)

 print(f'\nO valor da hipotenusa é: {a}')

medirHipotenusa()

#referenciando funções

def mostrarBatatas():
   print('batatas: doces, fritas, cozinhas ou esmagadas.')
   
mb = mostrarBatatas

#A variável mb é uma referência da função mostrarBatatas.
mb()

print(f'O que tem dentro de [mb]?:\n{mb}\n')


print(f'Tipo     [mb]: {type(mb)}')

print(f'Indice   [mb]: {id(mb)}\n')

print(f'Tipo   [mostrarBatatas]: {type(mostrarBatatas)}')

print(f'Indice [mostrarBatatas]: {id(mostrarBatatas)}')


import random

for i in range(1,6):
 #Randint -> Sorteia um nº inteiro entre x e y
 a = random.randint(0,10) #neste caso, x = 0 e y = 10

 #Exibe esse nº na tela.
 print(f'{i}º nº: {a}')

 
#def medidaHip(b, c):
 #Usa os valores de b e c na fórmula e devolve o resultado.
# return int(((b**2) + (c**2))**0.5)

#print('''
#Considerando que um triângulo retângulo (◣) possui três lados (A, B e C)
#e que "B" e "C" são catetos, elabore um programa que receba as suas medidas,
#
#calcule e exiba o valor da hipotenusa.
#
#fórmula: (a² = b² + c²)
#''')

#Pega os valores com o usuário
#cateto_b = int(input("\nDigite o tamanho do lado B: \n"))
#cateto_c = int(input("\nDigite o tamanho do lado C: \n"))

#Depois envia eles para a função e aguarda o resultado.
#hip_a = medidaHip(cateto_b, cateto_c)

#print(f'\nA medida da hipotenusa é: {hip_a};')

numeros = [1,2,3,4,5,6,7,8,9]

#Soma todos os elementos da lista números:
print(sum(numeros)) #Obs. o resultado dessa conta é 45

#Para usar uma variável como empacotador, basta

#adicionar um asterisco (*) antes do seu nome.

def soma(* num:int) -> int:
 '''
   A função Soma() recebe N números inteiros e retorna a soma de todos eles.


    Exemplo 01: soma(1,2)   -> 3

    Exemplo 02: soma(3,4,5) -> 12


    fórmula: s = y + … N
 '''
 resultado = 0

 for n in num:
   
   resultado += n

 return resultado

#Passando diferentes quantidades de parâmetros para função Soma():
print('Somando 1 Parâmetro ', soma(0)      ) #0
print('Somando 2 Parâmetros', soma(1, 2)   ) #3
print('Somando 3 Parâmetros', soma(3, 4, 5)) #12
print('Somando 4 Parâmetros', soma(6,7,8,9)) #30

def exemplo (* letras:str) -> list:
        return list(letras)

#caps é uma palavra-chave ou parâmetro nomeado, cujo valor padrão é False.

def acheABatata(* listaPalavras: str, caps = False) -> str:
 '''
   Essa função recebe N palavras e busca pela posição da palavra
   'batata'. Mas caso o valor de caps seja True, ela vai

    buscar por 'Batata', com 'B' maiúsculo.

   Exemplo:
     acheABatata('a, batata','maça')
     retorna: 'batata' é a 2º palavra!


      acheABatata('U','Maça', 'Batata', caps = True)
     retorna: 'Batata' é a 3º palavra!


      acheABatata('U','Maça', 'Cebola', caps = True)
     retorna: 'Não há uma Batata nessa lista T.T'  
 '''
 if caps == True:

     

        batata = 'Batata'
 else:

        batata = 'batata'

     

 if batata in listaPalavras:

     

        idBatata = listaPalavras.index(batata)

   

        return f'Batata é a {idBatata+1} palavra!'

   

 else:

        return f'Não há uma {batata} nessa lista T.T'



#Depois que todos os valores desejados são passados, podemos mudar o valor da palavra-chave

#chamando por ela.
print(acheABatata('Uva','Pera','Batata', caps = True))

#Emoticon é a variável opcional desta função.

def mensagem(msg:str, emoticon = ' '):
 '''
 Essa função exibe uma mensagem para o usuário. Se desejar,
 ela também pode exibir um emoticon.
 '''

 print(f'\n{msg}')

  #Então por padrão a mensagem sempre será exibida sem um emoticon,

  #Mas se o usuário inserir um valor diferente do padrão.
 if emoticon != ' ':
   print(f'\n{emoticon}') #Esse emoticon vai aparecer na tela.

mensagem('Olá Mundo')
mensagem('Tudo bem?', '😄')

#Obs.
#No Windows, ao pressionar as teclas (Windows + '.') uma lista de emoticons

#como este 😍 surgirá e você pode usá-los em quase todos os campos de texto.

#O 1º parâmetro dessa função é o X e o 2º é o Y.

def test(x,y):
   print(f'X:{x} / Y:{y} | A Soma de XY é: {x+y}')

#Então pela posição dos valores, sabemos que X é igual a 5 e Y é igual a 3.    
test(5,3)

#Mas podemos inverter a ordem, passando esses valores pelo nome dos seus parâmetros.
test(y = 2, x = 4)