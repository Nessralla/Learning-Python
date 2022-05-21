h1,m1,h2,m2 = input().split()
h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)
horas = 0
minutos = 0

if h1 == h2:
  if m2 > m1:
    
    horas = 0
    minutos = m2-m1
    
  elif m1>m2:
    
    horas = 23
    minutos = 60 - m1 + m2
  else:
    
    horas = 24
    
elif h1>h2:
  
  horas = 24-h1+h2
  if m1>m2:
    
    horas -=1
    minutos = 60-m1+m2
  elif m1<m2:
    
    minutos = m2 - m1
  else:
   
    minutos = 0



elif h1<h2:
  
  horas = h2 - h1
  if m1>m2:
    
    horas -=1
    minutos = 60-m1+m2
  elif m1<m2:
    
    minutos = m2-m1
  else:
   
    minutos=0



    
print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")