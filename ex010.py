# Conversor de Dólares
# Programa que lê quanto dinheiro uma pessoa tem na carteira e mostra quantos dólares ela pode comprar com esta quantia
# Considerando US$ 1,00 = R$ 5,26

n = float(input('Digite quanto de dinheiro você tem na sua carteira: '))
dolar = n // 5.26

print('A quantidade de dólares que você pode comprar é {}'.format(dolar))