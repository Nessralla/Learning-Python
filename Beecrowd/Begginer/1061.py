# Event Time

dia1 = input().split()
horario1 = input().split()
dia2 = input().split()
horario2 = input().split()

dia1 = int(dia1[1])
dia2 = int(dia2[1])
hora1 = int(horario1[0])
minuto1 = int(horario1[2])
segundo1 = int(horario1[4])
hora2 = int(horario2[0])
minuto2 = int(horario2[2])
segundo2 = int(horario2[4])

tSegundos1 = dia1*86400 + hora1*3600 + minuto1*60 + segundo1

tSegundos2 = dia2*86400 + hora2*3600 + minuto2*60 + segundo2

tSegundosTotal = tSegundos2 - tSegundos1

dias = tSegundosTotal//86400
tRestante = tSegundosTotal%86400
horas = tRestante//3600
tRestante = tRestante%3600
minutos = tRestante//60
tRestante = tRestante%60
segundos = tRestante

print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(F"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")