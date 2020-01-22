import random

keepGoing = True
repeats = 0
acertos = 0
erros = 0

while keepGoing == True :
    numRand = random.randint(1,9)
    numUser = int(input("Digite um numero de 1 a 9: "))

    if numUser < numRand : 
        print(f"Too low! O numero era {numRand}")
        erros = erros+1
    elif numUser > numRand :
        print(f"Too high! O numero era {numRand}")
        erros = erros+1
    elif numUser == numRand :
        print(f"Acertou miseravi! O numero era {numRand}")
        acertos = acertos+1
    repeats = repeats+1

    desejaSair = input("Deseja jogar mais uma vez? <s/n>")
    if desejaSair == 'n':
        keepGoing = False

print(f'Tentativas: {repeats}   |   Acertos: {acertos}   |   Erros: {erros}')

