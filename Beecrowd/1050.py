ddd = int(input())

dicionario = {61:'Brasilia',71:'Salvador',11:'Sao Paulo',21:'Rio de Janeiro',32:'Juiz de Fora',19:'Campinas',27:'Vitoria',31:'Belo Horizonte'}

if ddd not in dicionario:
  print("DDD nao cadastrado")
else:
  print(dicionario[ddd])