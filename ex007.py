# Programa que lê as duas notas de um aluno, calcula e mostra a sua média

nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1+n2)/2

print('O aluno {} obteve {:.2f} de primeira nota e {:.2f} de segunda nota, otendo uma média final de {:.2f}'.format(nome,n1,n2,media))