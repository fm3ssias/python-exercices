import random

a = random.sample(range(10), random.randint(0, 10)); b = random.sample(range(10), random.randint(0, 10));c=[]; c = [num1 for num1 in a for num2 in b if num1 == num2 if num1 not in c]; print(f'Lista a ={a}\nLista b = {b}\nElementos em comum entre eles sem repetições = {c}')


