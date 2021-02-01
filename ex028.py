# Programa que faz o computador “pensar” em um número inteiro entre 0 e 5 e pede para que o usuário tente
# descobrir qual foi o número escolhido pelo computador. O programa escreve na tela se o usuário venceu ou perdeu.


from random import randint # A função randint escolhe aleatoriamente um numero inteiro
from time import sleep
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5, tente advinhar!')
print('-=-'*20)
print('PENSANDO...')
sleep(5)                #O tempo de espera será de 5 segundos
print('-=-'*20)
print('PROCESSANDO...')
sleep(4)
print('-=-'*20)
n = int(input('Pensei em qual numero? '))
cpu = randint(0,5) # O range da busca aleatoria é entre 0 e 5

if n == cpu:
    print('Parabéns você me venceu!')
else:
    print('Você perdeu! Eu pensei no numero {}'.format(cpu))
