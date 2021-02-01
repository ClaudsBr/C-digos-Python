# Programa que calcula o IMC de uma pessoa e retorna seu grau de obesidade

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
IMC = peso / (altura*altura)

if IMC < 18.5:
    print('\33[1;35mAbaixo do peso!')
elif 18.5 <= IMC < 25:
    print('\33[1;34mPeso Ideal')
elif 25 <= IMC < 30:
    print('\33[1;33mSobrepeso')
elif 30 <= IMC < 40:
    print('\33[1;35mObesidade')
else:
    print('\33[1;31mObesidade Mórbida')
