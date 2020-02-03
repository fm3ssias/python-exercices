import random

def firstAndLastItem(lista) :
    return lista[0], lista[len(lista)-1]

list = random.sample(range(10), random.randint(0,10))
novaLista = firstAndLastItem(list)

print(f'Lista: {list}\nPrimeiro e último valor: {novaLista}')

