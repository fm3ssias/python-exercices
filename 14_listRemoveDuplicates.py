import random

# Funções
def remove_duplicates_set(lista):
    novaLista = set(lista)
    return list(novaLista)

def remove_duplicates_loop(lista):
    novaLista = []
    for el in lista:
        if el not in novaLista:
            novaLista.append(el)
    return novaLista
    
# Main
lista = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4]
print(f'Lista original: {lista}')
print(f'Usando set (set): {remove_duplicates_set(lista)}')
print(f'Usando set (loop): {remove_duplicates_loop(lista)}')