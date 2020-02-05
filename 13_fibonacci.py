def getNumero() :
    return int(input("Quantos numeros de fibonnaci vc quer gerar?"))

def getFibonnaci(qntdFib):
    ultimo = 1
    penultimo = 1
    lista = [1,1]

    for i in range(qntdFib):
        termo = penultimo + ultimo
        lista.append(termo)
        penultimo = ultimo
        ultimo = termo
    return lista

qntdFib = getNumero()
listaNumsFib = getFibonnaci(qntdFib)
print(listaNumsFib)