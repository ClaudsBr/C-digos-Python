# Programa que recebe a medida de 3 segmentos de reta e retorna se eles foram ou não um triangulo.
# Caso formem um triangulo retorna se é escaleno, equilatero ou isoceles.

a = float(input('Digite a medida de um segmento de reta: '))
b = float(input('Digite a medida de outro segmento de reta: '))
c = float(input('Digite a medida de outro segmento de reta: '))

if a + b > c and a +c > b and b + c > a:
    if a == b and b == c:
        print('Esses 3 segmentos de reta formam um triangulo do tipo \33[1;34mEQUILÁTERO')
    elif a != b and a != c and b != c:
        print('Esses 3 segmentos de reta formam um triângulo do tipo \33[1;34mESCALENO')
    else:
        print('Esses 3 segmentos de reta formam um triângulo do tipo \33[1;34mISÓCELES')
else:
    print('Esses 3 segmentos de reta \33[1;31mNÃO formam um triângulo')