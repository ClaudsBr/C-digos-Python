preco = float(input('Digite o Preço do produto: '))
cond_pag = int(input('Condição de pagamento:\n 1 - Dinheiro \n 2 - Cheque \n 3 - Cartão de crédito (à vista) \n '
                      '4 - Cartão de crédito (2 vezes) \n 5 - Cartão de crédito (3 vezes)\n '))

total = 0

if cond_pag == 1 or cond_pag == 2:
    total = preco * 0.9
    print('Você terá 10% de desconto e o total a ser pago será R$ {:.2f}'.format(total))
elif cond_pag == 3:
    total = preco * 0.95
    print('Você terá 5% de desconto e o total a ser pago será R$ {:.2f}'.format(total))
elif cond_pag == 4:
    print('O total a ser pago será R$ {:.2f} em duas parcelas de R$ {:.2f}'.format(preco,preco/2))
elif cond_pag == 5:
    total = preco*1.2
    parcela = total/3
    print('Você terá 20% de juros e o total a ser pago será R$ {:.2f} em 3 parcelas de R$ {:.2f}'.format(total, parcela))