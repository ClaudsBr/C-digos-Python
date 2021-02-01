# Programa que recebe dois valores inteiros e retona qual é o maior ou se são iguais

a = int(input("Digite um número inteiro: "))
b = int(input('Digite outro número inteiro: '))

if a > b :
    print('O \33[1;34mprimeiro\33[m valor é o maior!')
elif a < b :
    print('O \33[1;34msegundo \33[mvalor é o maior!')
else:
    print('\33[1;31mNão existe\33[m valor maior, os dois valores são \33[1;34miguais')