# Programa que lê o nome completo de uma pessoa e mostra:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo(sem considerar espaços)
# Quantas letras tem o primeiro nome.

nome = (input('Digite seu nome completo: '))
NOME = nome.upper()
nominho = nome.lower()
espaco = nome.count(' ')
tamanho = len(nome)
caract = tamanho - espaco
dividida = nome.split()
palavra = dividida[0]
print(NOME)
print(nominho)
print(caract)
print(len(palavra))

