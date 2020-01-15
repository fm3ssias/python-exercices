palavra  = input("Digite uma palavra para saber se ela é palindromo ou não: ")
isPalind = True

if len(palavra)%2 == 0:
    for a in range(int(len(palavra)/2)):
        if palavra[a] != palavra[((len(palavra)-1)-a)] :
            isPalind = False
            break
else:
    for a in range(int(((len(palavra)-1)/2))):
        if palavra[a] != palavra[((len(palavra)-1)-a)] :
            isPalind = False
            break
        
print(f"A palavra {palavra} é um Palindromo!" if isPalind else f"A palavra {palavra} é um Palindromo!") #Ternário. <expressao1> if <condicao> else <expressao2>