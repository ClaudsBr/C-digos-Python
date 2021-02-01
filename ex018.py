# Programa que lê um ângulo qualquer a mostra na tela o valor do seno, docosseno e da tangente desse ângulo.

from math import sin, cos, tan
angulo = int(input('Digite o valor do ângulo: '))

print('O ângulo de {}º tem o seno igual a {:.2f}, o cosseno igual a {:.2f} e a tangente igual a {:.2f}'.format(angulo,sin(angulo),cos(angulo),tan(angulo)))

