
personagens = {
#Sly Cat -> Gatinho Manhoso
"sly_cat" : f'''
     |\      _,,,---,,_
ZZZzz /,`.-'`'    -.  ;-;;,_
    |,4-  ) )-,_. ,\ (  `'-'
   '---''(_/--'  `-'\_)
'''
,
#Smelly Cat -> Gato Fedido
"smelly_cat" : f'''
_._     _,-'""`-._
(,-.`._,'(       |\`-/|
   `-.-' \ )-`( , o o)
         `-    \`_`"'-
'''
,
#Little Food -> Pouca comida
"little_food" : f'''
              __
             / _)
    _.----._/ /
   /         /
__/ (  | (  |
/__.-'|_|--|_|
'''}

def desenho(x):
    print(personagens[x])

desenho("little_food")