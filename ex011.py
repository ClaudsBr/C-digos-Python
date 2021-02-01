# Programa que lê a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

largura = float(input('Digite a largura em metros: '))
altura = float(input('Digite a altura em metros: '))
area = largura * altura
tinta = area / 2

print('A largura da parede é de {} metros, sua altura é {} metros, sua área {} metros e são necessarios {} litros de tinta para a pintura'.format(largura,altura,area,tinta))
