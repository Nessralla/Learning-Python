def leiaDinheiro():
    recebido = input("Digite o preço: R$ ")
    try:
        recebido = float(recebido)
        return recebido
    except:
        if "," in recebido:
            recebido = recebido.split(",")
            try:
                val1 = int(recebido[0])
                val2 = int(recebido[1])
                recebido = str(val1) + "." + str(val2)
                recebido = float(recebido)
                return recebido
            except:
                print(f"{recebido} é um preço inválido")
        else:
            print(f"{recebido} é um preço inválido")

leiaDinheiro()