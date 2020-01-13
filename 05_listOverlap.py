import random 
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = []
b = []
c = []

for x in range(1,10):
    a.append(random.randint(1,100))
    b.append(random.randint(1,100))

for primeiro in a: 
    if primeiro in b:
        if primeiro not in c:
            c.append(primeiro)

print (c)