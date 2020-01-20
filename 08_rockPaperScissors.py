import time

while True :
    cont = 0

    print('******************************')
    print('1-Pedra, 2-Papel e 3-Tesoura!!')
    print('******************************\n')
    j1 = int(input('Jogador 1: '))
    j2 = int(input('Jogador 2: '))

    while cont < 3 :
        print ('.', end=" ", flush=True)
        cont = cont + 1
        time.sleep(1)

    print('')
    if j1 == 1 and j2 == 2: 
        print ('Jogador 2 (Papel) vence Jogador 1 (Pedra)!')
    elif j1 == 1 and j2 == 3: 
        print ('Jogador 1 (Pedra) vence Jogador 2 (Tesoura)!')
    elif j2 == 2 and j1 == 3:
        print ('Jogador 1 (Tesoura) vence Jogador 2 (Papel)!')

    elif j1 == 2 and j2 == 1:
        print ('Jogador 1 (Papel) vence Jogador 2 (Pedra)!')
    elif j1 == 2 and j2 == 3:
        print ('Jogador 2 (Tesoura) vence Jogador 1 (Papel)!')

    elif j1 == 3 and j2 == 1:
        print ('Jogador 2 (Pedra) vence Jogador 1 (Tesoura)!')
    elif j1 == 3 and j2 == 2:
        print ('Jogador 1 (Tesoura) vence Jogador 2 (Papel)!')

    elif j1 == 1 and j2 == 1:
        print ('Jogador 1 (Pedra) empatou com o Jogador 2 (Pedra)!')
    elif j1 == 2 and j2 == 2:
        print ('Jogador 1 (Papel) empatou com o Jogador 2 (Papel)!')
    elif j1 == 3 and j2 == 3:
        print ('Jogador 1 (Tesoura) empatou com o Jogador 2 (Tesoura)!')

    keep = str(input ('Deseja jogar novamente? <y/n>'))

    if keep == 'n':
        break
    

