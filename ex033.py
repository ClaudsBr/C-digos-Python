# Programa que lê três números e mostra qual é o maior e qual é o menor.

n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
n3 = int(input('Digite o 3º número: '))


maior = n1
if n2 > n1:
    maior = n2
    if n3 > n2:
        maior = n3
menor = n3
if n2 < n3:
    menor = n2
    if n1 < n2:
        menor = n1

print('O maior número é o {}'.format(maior))
print('O menor número é o {}'.format(menor))