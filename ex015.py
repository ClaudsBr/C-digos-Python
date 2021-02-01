# Programa que pergunta a quantidade de Km percorridos por um carro alugado e a quantidade
# de dias pelos quais ele foi alugado. Calcula o preço a se pagar, sabendo que o carro custa R$ 60 por dia
# e R$ 0,15 por Km rodado.

print('          Aluguel do carro             ')
dia = int(input('Digite a quantidade de dias: '))
km = float(input('Digite a quantidade de Quilometros rodados: '))
p1 = dia * 60
p2 = km * 0.15

total = p1 + p2

print('O total a pagar é R$ {:.2f}'.format(total))
