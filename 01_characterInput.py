'''
Objetivo: Mostrar ao usuário em qual ano ele fara 100 anos
Entrada: Nome e idade
Saida: O ano que ele fará 100 anos
'''
from datetime import datetime

now = datetime.now()

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade atual: '))

diferencaIdade = 100 - idade
print(nome+", em "+str(now.year+diferencaIdade)+" você terá 100 anos!")

x = int(input("Agora digite a quantidade de vezes que deseja repetir a ultima mensagem: "))
print((nome+", em "+str(now.year+diferencaIdade)+" você terá 100 anos!\n")*x)