# Programa que lê o nome de uma cidade e diz se ela começa ou não com o nome ‘SANTO’

cidade = input('Digite o nome de sua cidade: ').strip() # strip é uma função usada para eliminar os espaços
print(cidade[:5].upper() == 'SANTO')

