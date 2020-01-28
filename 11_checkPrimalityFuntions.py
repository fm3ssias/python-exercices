def get_number(texto='Digite um numero: '):
    return(int(input(texto)))

isPrimo = True
num = get_number()
divisors = range(2,num)

for i in divisors:
    if num%i == 0:
        isPrimo = False

if isPrimo :
    print(f'O numero {num} é primo!')
else:
    print(f'O numero {num} não é primo!')