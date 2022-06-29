import timeit


RelCid = dict()

# na key, item 0 = quantidade de pessoas
# na key, item 1 = consumo total
# na key, item 2 = consumo por pessoa

# lista provisória para armazenar os consumos
listProv = list()
# iniciando as variáveis cidade e testcase
cidade = 1
testCase = 1

listDuplic = []

# neste loop inserimos os dados no dicionário
while True:
  testCase = int(input())
  # O programa termina quando for digitado 0
  if testCase == 0:
      break
  # Senão criamos uma lista para receber os valores de habitantes e consumo da cidade
  else:
    RelCid["cidade"] = list()
    # Agora precisamos receber os valores de acordo com a quantidade de casas
    for i in range(testCase):
        temp = input().split()
        # Recebida a dupla de moradores e consumo, convertemos os valores para int
        temp[0] = int(temp[0])
        temp[1] = int(temp[1])
        # Calculamos o consumo por habitante, arredondando para baixo
        cons = int(temp[1]/temp[0])
        # Agora criamos uma lista dentro da lista mestre, guardando a quantidade da habitantes, o consumo e a media
        RelCid["cidade"].append(list())
        RelCid["cidade"][i].append(temp[0])
        RelCid["cidade"][i].append(temp[1])
        RelCid["cidade"][i].append(cons)

    # Neste loop fazemos o programa após armazenarmos todas as informações
    
    # Imprimimos a cidade
    print(f"Cidade# {cidade}:")
    # Criamos uma lista provisória para manipular os dados
    listProv = [[],[],[]]
      
    # Para cada casa na relação de casas da cidade i, copiamos os dados para uma outra lista, agrupando as informações
    # No [0] ficarão todos os habitantes da cidade, no [1] fica a média, no [2] fica o consumo
    for i in range(len(RelCid["cidade"])):
      listProv[0].append(RelCid["cidade"][i][0])
      listProv[1].append(RelCid["cidade"][i][2])
      listProv[2].append(RelCid["cidade"][i][1])
      
    # Agora somamos o total de habitantes e total consumido na cidade
    totalHab = sum(listProv[0])
    totalCons = sum(listProv[2])
      
    # Pode ocorrer de ter alguma casa ter consumo igual, portanto devem ser agrupadas. Por isso precisamos
    # da lista duplicada
    while len(listProv[1]) > 0:
      # Aqqui vamos rodar o código para encontrar o menor valor
      menor = min(listProv[1])
      ind = listProv[1].index(menor)
      a = listProv[1].count(menor)

      # Aqui verificamos se tem mais de uma casa com consumo igual, se sim duplicamos a lista e removemos o dado
      # da listaProv, O consumo deve ser mostrado do menor para o maior, por isso retornamos o menor, imprimimos
      # e deletamos após a impressão.
      if a > 1:
          for i in range(a):
              listDuplic.append(listProv[0][ind])
              b = listProv[1][ind]
              del listProv[0][ind]
              del listProv[1][ind]
          print(f"{sum(listDuplic)}-{b}",end=' ')
            
      # Se não tiver, é só mostrar o valor real    
      else:
          print(f"{listProv[0][ind]}-{listProv[1][ind]}",end=' ')
          del listProv[0][ind]
          del listProv[1][ind]
    print("")
    valor = totalCons/totalHab
    valor = str(valor)
    print(f"Consumo medio: {valor[:5]} m3. \n")
    RelCid["cidade"].clear()
    listProv.clear()
    
    # Após percorrer todas as casas informadas, voltamos para nosso loop incrementando a contadora de cidades
    cidade += 1



