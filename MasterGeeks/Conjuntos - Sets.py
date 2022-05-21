#Lista de Suspeitos

from cmath import pi


suspeitos = [

#Nome:            Sexo: Cabelo:  Altura:  Peso:        Hooby:
('Anita Bath',      'F', 'Ruivo',  'Alto', 'Sobrepeso', 'Jogos de Azar'), #0
('Anne Arthy',      'F', 'Loiro', 'Baixo',    'Normal',    'Jardinagem'), #1
('Barb Dwyer',      'M', 'Loiro', 'Medio', 'Sobrepeso',      'Esportes'), #2
('Catherine Stark', 'F', 'Preto', 'Medio',     'Magro',         'Artes'), #3
('Constantino B.',  'F', 'Preto',  'Alto',     'Magro',    'Literatura'), #4
('Olena Mendes',    'F', 'Calvo', 'Baixo',    'Normal',          'Moda'), #5
('Peter P.',        'M', 'Preto', 'Medio',    'Normal',    'Fotografia'), #6
('Sr.Bozzo',        'M', 'Calvo',  'Alto', 'Sobrepeso',    'Tecnologia'), #7
('Tenorio Salazar', 'M', 'Ruivo', 'Baixo',     'Obeso',       'Caçador'), #8
('W. Lionheart',    'F', 'Loiro', 'Medio',    'Normal',       'Felinos')]

homens = set()
mulheres = set()
ruivos = set()
loiros = set()
pretos = set()
calvos = set()
altos = set()
baixos = set()
medios = set()
pNormal = set()
magro = set()
sobrepeso = set()
obeso = set()

mandato = set()




#lista de homens e mulheres
for i in range(len(suspeitos)):
    if suspeitos[i][1] == 'M':
        homens.add(suspeitos[i][0])
    else:
        mulheres.add(suspeitos[i][0])

#lista de tipos de cabelo
for i in range(len(suspeitos)):
    if suspeitos[i][2] == "Ruivo":
        ruivos.add(suspeitos[i][0])
    elif suspeitos[i][2] == "Calvo":
        calvos.add(suspeitos[i][0])
    elif suspeitos[i][2] == "Preto":
        pretos.add(suspeitos[i][0])
    else:
        loiros.add(suspeitos[i][0])

#lista de altura
for i in range(len(suspeitos)):
    if suspeitos[i][3] == "Alto":
        altos.add(suspeitos[i][0])
    elif suspeitos[i][3] == "Medio":
        medios.add(suspeitos[i][0])
    else:
        baixos.add(suspeitos[i][0])

#lista de peso
for i in range(len(suspeitos)):
    if suspeitos[i][4] == "Normal":
        pNormal.add(suspeitos[i][0])
    elif suspeitos[i][4] == "Magro":
        magro.add(suspeitos[i][0])
    elif suspeitos[i][4] == "Sobrepeso":
        sobrepeso.add(suspeitos[i][0])
    else:
        obeso.add(suspeitos[i][0])


pistas = (
 '\n1º Pista: \n O suspeito foi visto entrando em um carro, rumo ao aeroporto\n',
 
 '\n2º Pista: \n Na cena do crime, uma testemunha afirmou que o ladrão tinha mãos femininas\n',

 '\n3º Pista: \n Antes de embarcar, o suspeito fugiu pelos dutos de ar do aeroporto.\n',

 '\n4º Pista: \n A bagagem deixada para trás era uma bomba, \n'+
 'mas encontramos um fio loiro em seus destroços.\n',
   
 '\n5º Pista: \n A amostra de DNA não pode ser concluída, \n'+
 'mas uma de suas botas continha um passe para o Parque Nacional Kruger.\n',

 '\n6º Pista: \n Aos arredores do Parque, um turista foi visto em posse de uma jóia.\n'+
 'Ele tinha uma altura mediana e estava conversando com Traficantes de Marfim.\n',

 '\nFim de Jogo: \n O suspeito foi capturado em uma emboscada, \n'+
 'pegamos ela com a esmeralda, em uma das trilhas do Safári.\n'

)

print("""\n Um colar de esmeraldas, que pertenceu à princesa Isabel, foi furtado do Museu Nacional Quinta da 
    Boa Vista, localizado no Rio de Janeiro e recentemente recuperado de um incêndio. O furto ocorreu durante 
    um evento internacional que, por meio da exposição das jóias da família real, tentava angariar fundos 
    para a ampliação e restauração do acervo do museu. Por enquanto a polícia segue investigando o caso, 
    mas os suspeitos não tiveram seus nomes divulgados. \n""")

print("Lista de suspeitos e suas características \n")
for i in suspeitos:
    print(i,"\n")

print(pistas[0])
print("\n Todos são suspeitos \n")
print(pistas[1])
print("\nSuspeitas mulheres:\n",mulheres)
print(pistas[2])
print("\nSuspeitos que não são gordos: \n",mulheres&(magro|pNormal))
print(pistas[3])
print("\nSuspeitos que são loiros: \n",mulheres&(magro|pNormal)&loiros)
print(pistas[4])
print("As duas ainda continuam suspeitas")
print(pistas[5])
print("A suspeita é: ",mulheres&loiros&medios&(magro|pNormal))