# Programa que lê um número Real qualquer pelo teclado e mostra na tela a sua porção Inteira.
# Ex: Digite um número: 6.127
#       O número 6.127 tem a parte Inteira 6.

from math import trunc
numero = float(input('Digite um numero: '))

print('A parte inteira do numero {} é {}'.format(numero,trunc(numero)))
