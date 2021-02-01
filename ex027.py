# Programa que lê o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
#    primeiro = Ana
#    último = Souza

nome_completo = input('Digite seu nome completo: ').strip()
nome = nome_completo.split()
primeiro_nome = nome[0]
ultimo_nome = nome[-1]

print('Seu nome completo é {}'.format(nome_completo))
print('Seu primeiro nome é {}'.format(primeiro_nome))
print('Seu ultimo nome é {}'.format(ultimo_nome))