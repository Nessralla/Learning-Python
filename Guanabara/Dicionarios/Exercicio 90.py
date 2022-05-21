#Elabora um programa que leia nome e a media do aluno guardando tambem a situação em um dicionário.>=7.0 aprovado

relacao = list()
alunos = {}

from time import sleep

while True:
    alunos["nome"] = str(input("Digite o nome do aluno: "))
    alunos["nota"] = float(input("Digite a media da nota: "))
    if alunos["nota"] >= 7.0:
        alunos["situacao"] = "Aprovado"
    else:
        alunos["situacao"] = "Reprovado"
    relacao.append(alunos.copy())
    alunos.clear()
    opc = input("\n Deseja continuar cadastrando alunos? [S] ou [N]")
    if opc in "Nn":
        break
    else:
        sleep(0.5)
        print("Continuando o programa \n")
        sleep(0.5)

for a in range(len(relacao)):
    print(f"O aluno(a) {relacao[a]['nome']} teve a nota {relacao[a]['nota']}, sua situação é: {relacao[a]['situacao']}")