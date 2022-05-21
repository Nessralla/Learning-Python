# Como abrir, escrever, modificar arquivos

# o 'r' precisa vir antes do caminho do arquivo, sem virgula ou separação, para leitura
file = open(r"C:\Users\Usuario\MyApp\Learning Python\MasterGeeks\Banco.txt",'w')

#cont = file.read(100) # Armazenar o que foi lido na variável cont

# Após ler uma vez não é possível ler novamente, pois irá para o fim do texto. Retornando uma string vazia.

#print("Reading one bite")
#print(file.read(1)) # Por isso neste código temos o 'h'
#print("Reading two bites")
#print(file.read(2)) # E neste código o 'h' já foi lido, então passa para o 'e'
#print("Reading three bites")
#print(file.read(3))

# Para retornar as linhas separadamente, deve ser utiliando o comando file.readlines(), que retonar uma lista

a = file.write("Escrevi isso no arquivo") # No caso, ao abrir um arquivo no modo write, todo seu conteúdo é deletado.
print(a) # No caso é possível armazenar numa variável, i.e. 'a' para saber o total de bites utilizados 
file.close()

file = open(r"C:\Users\Usuario\MyApp\Learning Python\MasterGeeks\Banco.txt")
print(file.read())

#print("Tipo da variável: ",type(cont))

#print("Imprimir o arquivo inteiro")
#print(cont)
file.close()

# o with abre e fecha o arquivo. No caso só é possível acessar f dentro do with
with open("filename.txt") as f:
   print(f.read())