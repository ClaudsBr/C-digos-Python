# Algoritmo que lê o preço de um produto e mostra seu novo preço, com 5% de desconto

produto = float(input('Digite o preço do produto: '))
novo_preco = produto * 0.95

print('O preço do produto é {}, mas com nosso desconto de 5% seu novo preço é {}'.format(produto,novo_preco))
