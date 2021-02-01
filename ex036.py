#Programa recebe o valor de uma casa, o valor do salrio e a quantidade de anos em que será pago o financiamento
# Retornando se o emprestimo será ou não aprovado.

print('\33[1;33;41m    Financiando uma Casa      \33[m')

casa = float(input(' Digite o valor da casa: '))
salario = float(input(' Digite o valor do seu salário: '))
anos = int(input('Digite a quantidade de anos que pretende pagar: '))

prestacao = salario * 0.3
total = 12*prestacao*anos
if total >= casa:
    print('\33[1;34mSeu emprestimo foi aprovado, PARABÉNS!')
else:
    print('\33[1;31mINFELIZMENTE seu empréstimo não foi aprovado.')


