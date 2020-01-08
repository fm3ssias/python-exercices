'''
Objetivo: Mostrar pro usuário se o numero inserido é par ou impar
Entrada: Um numero 
Saida: Se é impar ou par
'''

numero = 1

while numero != 0 :
    numero = int(input("Digite um numero (0 para sair): "))
    if numero == 0:
        break
    divPorQuatro = str(numero)
    if int(divPorQuatro[-2:])%4 == 0 or int(divPorQuatro[-2:]) == 00:
        print(f"O numero {numero} é divisivel por 4!")
    elif numero%2 == 0:
        print(f"O numero {numero} é par!")
    else:
        print(f"O numero {numero} é impar!")