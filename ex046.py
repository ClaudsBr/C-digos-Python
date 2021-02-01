# Contagem regressiva

from time import sleep
print('\33[1;33mA queima de fogos começará em....')
sleep(3)
for cont in range (10,0, -1):
    print('\33[1;32m{}\33[m'.format(cont))
    sleep(1)
print('\33[1;34mFELIZ ANO NOVO!!!')