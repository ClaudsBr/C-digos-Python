# JOKENPOO

from random import randint
from time import sleep


jogador = int(input('JOKENPO:\n [0] - PEDRA\n [1] - PAPEL \n [2] - TESOURA \n '))
print('\33[7;34;40mJO\33[m')
sleep(2)
print('\33[1;34;41mKEN\33[m')
sleep(2)
print('\33[7;34;40mPOO...\33[m')
sleep(4)
item = ('PEDRA','PAPEL','TESOURA')
computador = randint(0,2)

if (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
    print('\33[1;34mVocê VENCEU!\33[m \n Você escolheu \33[4;34m{}\33[m \n o Computador escolheu \33[0;31m{}'.format(item[jogador],item[computador]))
elif (jogador == 0 and computador == 1) or (jogador == 1 and computador == 2) or (jogador == 2 and computador == 0):
    print('\33[1;31mVocê PERDEU!\33[m \nVocê escolheu \33[4;31m{}\33[m \n o Computador escolheu \33[0;34m{}'.format(item[jogador], item[computador]))
else:
    print('\33[1;32mEMPATE!\33[m \n Você escolheu \33[4;32m{} \33[m\n O Computador escolheu \33[4;32m{}'.format(item[jogador],item[computador]))

