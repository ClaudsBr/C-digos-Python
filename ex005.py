# Programa que lê um número inteiro e mostra na tela o seu sucessor e seu antecessor

n = int(input('Digite um numero inteiro: '))
ant = n - 1
suc = n + 1
print('O numero digitado foi {}, seu antecessor é {} e seu sucessor é {}'.format(n,ant,suc))