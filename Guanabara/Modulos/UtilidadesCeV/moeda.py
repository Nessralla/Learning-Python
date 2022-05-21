def metade(valor, trans = False):
    if trans == True:
        return (moeda(valor/2))
    return valor/2

def dobra(valor, trans = False):
    if trans == True:
        return (moeda(valor*2))    
    return valor*2

def aumentar(valor, porc, trans = False):
    if trans == True:
        return (moeda(valor*((100+porc)/100)))    
    return valor*((100+porc)/100)

def reduzir(valor, porc, trans = False):
    if trans == True:
        return (moeda(valor*((100-porc)/100)))
    return valor*((100-porc)/100)

def resumo(valor, p1, p2, trans = False):
    res = dict()
    if trans == True:
        res["Preço analisado"] = moeda(valor)
        res["Valor dobrado"] = dobra(valor, True)
        res["Metade do preço"] = metade(valor, True)
        a = str(p1) + "% de aumento"
        res[a] = aumentar(valor, p1, True)
        a = str(p2) + "% de redução"
        res[a] = reduzir(valor, p2, True)
    for k,v in res.items():
        print(f"{k}\t\t{v:>5}")

        
    dobrado = dobra(valor, False)
    metado = metade(valor, False)
    aumentado = aumentar(valor, p1, False)
    reduzido = reduzir(valor, p2, False)
    return dobrado, metado, aumentado, reduzido    

def moeda(valor: float):
    return f"R$ {valor:.2f}".replace(".",",")
