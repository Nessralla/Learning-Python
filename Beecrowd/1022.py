# Seu programa irá receber n operações com frações, podendo ser uma das 4 operações
# Ao final das contas, deve simplificar a fração

# Primeiro pegamos quantas frações iremos receber
cases = int(input())

# Então criamos todas as variáveis que serão utilizadas
n1 = 0
d1 = 0
n2 = 0
d2 = 0
n1A = 0
n2A = 0
d1A = 0
d2A = 0
barra = ""
op = ""
# Variáveis para cálculo do MDC
maior = 0
menor = 0
resto = 1

# Função para calcular o MDC
def mdc(x,y):
  if x>y:
    maior = x
    menor = y
  else:
    maior = y
    menor = abs(x)
  while True:
    if x == 0:
      n2A = 0
      d2A = 1
      menor = 1
      y = d2A
      break
    resto = maior%menor
    if resto == 0:
      break
      # sai do while pois sabemos que o valor menor é o MDC.
    maior = menor
    menor = resto
  n2A = int(x/menor)
  d2A = int(y/menor)
  return n2A,d2A


# Separamos os valores pelas variáveis
for i in range(cases):
  n1,barra,d1,op,n2,barra,d2 = input().split()
  n1,d1,n2,d2 = int(n1),int(d1),int(n2),int(d2)

# print(base)
  if op == "+":
    n1A = n1*d2+n2*d1
    d1A = d1*d2
    # Agora utilizamos a formula para saber qual é o MDC para simplificar a fração
    n2A, d2A = mdc(n1A,d1A)

  elif op == "-":
    n1A = n1*d2-n2*d1
    d1A = d1*d2
    # Agora utilizamos a formula para saber qual é o MDC para simplificar a fração
    n2A, d2A = mdc(n1A,d1A)

  elif op == "*":
    n1A = n1*n2
    d1A = d1*d2
    # Agora utilizamos a formula para saber qual é o MDC para simplificar a fração
    n2A, d2A = mdc(n1A,d1A)

  elif op == "/":
    n1A = n1*d2
    d1A = n2*d1
    # Agora utilizamos a formula para saber qual é o MDC para simplificar a fração
    n2A, d2A = mdc(n1A,d1A)

  # Ao final de cada iteração, imprimimos o resultado da operação
  print(f"{n1A}/{d1A} = {n2A}/{d2A}")