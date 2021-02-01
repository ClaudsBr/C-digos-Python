soma = 0
cont = 0
for n in range (1,6+1):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont +1
print('A somatoria entre os valores pares digitados é {}'.format(soma))
