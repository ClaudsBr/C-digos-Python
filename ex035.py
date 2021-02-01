# Programa que lê o comprimento de três retas e diz ao usuário se elas podem ou não formar um triângulo


lado1 = int(input('Digite a medida de um segmento de reta: '))
lado2 = int(input('Digite a medida de outro segmento de reta: '))
lado3 = int(input('Digite a medida de outro segmento de reta: '))

if lado1 + lado2 > lado3 and lado1 + lado3 and lado2 + lado3 > lado1:
    print('O 3 segmentos de reta digitados formam um TRIÂNGULO')
else:
    print('Os 3 segmentos de reta digitados NÃO formam um Triângulo')