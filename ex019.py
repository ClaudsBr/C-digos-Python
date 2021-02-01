# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Este programa o ajuda lendo os nomes
# deles e escrevendo o nome do escolhido na tela

import random

a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
lista = [a1,a2,a3,a4]
escolhido = random.choice(lista) #A funçao choice escolhe um elemento

print('O aluno escolhido foi {}'.format(escolhido))