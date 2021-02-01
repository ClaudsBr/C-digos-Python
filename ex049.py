# Tabuada com o laço for

n = int(input('Digite o numero e te mostrarei sua tabuada: '))
print('\33[1;31mTabuada do {}!\n\33[m '.format(n))

for cont in range (0, 10+1):
    print('\33[1;34m{} x {:2} = {:2}'.format(n,cont,n*cont))