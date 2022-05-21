alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z']
lista = []

def range_alfabeto(x,y):
    
    if x not in alfabeto or y not in alfabeto:
        return print(alfabeto[0])

       
    a = alfabeto.index(x)
    b = alfabeto.index(y)
    if a>b:
        for i in range(a,b-1,-1):
            lista.append(alfabeto[i])
        print(lista)
            
    elif a<b:
        for i in range(a,b+1):
            lista.append(alfabeto[i])
        print(lista)
    elif a==b:
        print(x)

range_alfabeto('2','c')
