import random 

# Funções
# Solução do exercicio 14
def usandoSet(a, b):
    setA = set(a) 
    setB = set(b)

    for primeiro in setA: 
        if primeiro in setB:
            if primeiro not in c:
                c.append(primeiro)

    return c

# Main
# Solução original
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = []
b = []
c = []

for x in range(10,25):
    a.append(random.randint(10,20))
    b.append(random.randint(10,20))
''' 
for primeiro in a: 
    if primeiro in b:
        if primeiro not in c:
            c.append(primeiro)
'''
usandoSet(a, b)

print(f'a:{a}')
print(f'a:{b}')
print(f'c:{c}')