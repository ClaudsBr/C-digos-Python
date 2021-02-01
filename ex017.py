# Programa que lê o comprimento do cateto oposto e do cateto adjacente de um triângulo,
# calcula e mostra o comprimento da hipotenusa.

from math import sqrt, trunc
catOp = int(input('Digite o valor do cateto oposto do triangulo retângulo: '))
catAd = int(input('Digite o valor do cateto adjacente do triangulo retângulo: '))
Hip= (catOp**2 + catAd**2)**(1/2)
print('O triangulo retângulo de cateto oposto igual a {} e cateto adjacente igual a {} tem a hipotenusa medindo {}'.format(catOp,catAd,trunc(Hip)))
