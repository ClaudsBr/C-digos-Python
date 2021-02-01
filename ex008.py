# Programa que lê um valor em metros e o exibe convertido em centímetros e milímetros

n = float(input('Digite um valor em metros: '))
centi = n * 100
mili = n * 1000

print('{} metros equivalem a {:.1f} centímetros e {:.1f} milímetros'.format(n,centi,mili))