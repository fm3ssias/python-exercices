'''a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
limite = 5

for i in range(len(a)):
    if a[i] < 5:
        b.append(a[i])

print(f"Lista a = {a}")
print(f"Lista c/ nº menores que {limite}, b = {b}")'''

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]; print([aa for aa in a if aa < 5])

