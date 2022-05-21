pTermo = int(input("Digite o primeiro termo: "))

razao = int(input("Digite a razão: "))

# Razao = 4
# Termo1 = 2
# Termo2 = 4 * Termo1 (8)
# Termo3 = 4 * Termo2 (32)
# ...

def termo(n,ter,raz):
    """
    Função para calcular o enésimo termo de acordo com o desejado pelo usuário. Usando função recursiva. 
    n = qual termo o usuário deseja
    ter = primeiro termo
    raz = razão da multiplicação
    """
    if n == 1:
        return ter
    else:
        return termo(n-1,ter,raz)*raz

qTermo = int(input("Digite o termo que deseja da operação: "))

print(termo(qTermo,pTermo,razao))
