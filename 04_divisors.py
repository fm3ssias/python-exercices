num = int(input("Digite um numero: "))
divisors = range(1,num+1)

for i in divisors:
    if num%i == 0:
        print(i)

#print(f"{divisors} são divisiveis por {num}!" )