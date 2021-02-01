# Programa que lê uma frase pelo teclado e mostra:
# Quantas vezes aparece a letra ‘A’
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece a última vez

frase = input('Digite uma frase: ').strip()
A = frase.upper().count('A')
A1 = frase.upper().find('A')
Au = frase.upper().rfind('A')  # o comando rfind() começa a procura pelo caractere pela direta
print('A letra A aparece {} vezes na frase'.format(A))
print('A primeira letra A apareceu na posição {}'.format(A1))
print('A ultima letra A apareceu na posição {}'.format(Au))

