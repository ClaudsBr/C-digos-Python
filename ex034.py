# Programa que pergunta o salário de um funcionário e calcula o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcula um aumento de 10%. Para os inferiores ou iguais,
# o aumento é de 15%.

salario = float(input('Digite o valor do seu salário: '))
aumento = 0
if salario <= 1250:
    aumento = 15
    novo_salario = salario * 1.15
else:
    novo_salario = salario *1.1
    aumento = 10

print('Seu novo salário com o aumento de {}% será R$ {:.2f}'.format(aumento,novo_salario))