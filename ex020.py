# O mesmo professor do ex19.py quer sortear a ordem de apresentação de trabalhos dos alunos.
# Este programa que lê os nomes dos quatro alunos e mostra a ordem sorteada.

import random

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')

lista = [a1, a2, a3, a4]
random.shuffle(lista) #Shuffle quer dizer embaralhar
print(lista)