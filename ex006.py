# Algoritmo que lê um número e mostra o seu dobro, seu triplo e sua raiz quadrada

n = int(input('Digite um numero inteiro: '))
dobro = n + n
triplo = 3 * n
raiz = n ** 0.5

print('O numero digitado foi o {}, seu dobro é {}, seu triplo {} e sua raiz quadrada é {:.2f}'.format(n, dobro, triplo, raiz))