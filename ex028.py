from random import randint
from time import sleep

computador = randint(0,5)
print('-=-' * 20)
print('Estou pensando em um número entre \033[34m0\033[m e \033[36m5\033[m')
print('-=-' * 20)
usuario = int(input('Tente adivinhar o número: '))
print('Analisando...')
sleep(2)
if computador == usuario:
    print('Você \033[1;33mganhou\033[m, dessa vez...')
else:
    print('Eu venci!')
print(f'O numero escolhido foi \033[31m{computador}\033[m')
