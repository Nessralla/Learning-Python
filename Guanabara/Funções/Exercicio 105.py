# Crie um programa que recebe várias notas de alunos, retornando um dicionário com a quantidade de notas.
# A maior nota, a menor nota, a media da turma, a situação(opcional). Adicionar também docstrings

from inspect import BoundArguments


def notas(*n,sit=False):
    """Função para calcular notas, media, maior e menor notas dos alunos, bem como a situação
    n: empacotador para receber todas as notas
    sit(opcional): exibir ou não a situação
    return = o dicionário todas"""
    todas = dict()
    todas["total"] = len(n)
    todas["maior"] = max(n)
    todas["menor"] = min(n)
    todas["media"] = float(sum(n)/len(n))
    if sit == False:
        return todas
    else:
        if todas["media"] >= 7:
            todas["situação"] = "BOA"
            return todas
        elif todas["media"]  >= 5:
            todas["situação"] = "RAZOÁVEL"
            return todas
        else:
            todas["situação"] = "RUIM"
            return todas



print(notas(8,5,2,7,8,10))
help(notas)