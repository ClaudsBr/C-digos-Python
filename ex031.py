# Programa que pergunta a distância de uma viagem em kms. Calcula o preço da passagem,
# cobrando R$ 0,50 por km para viagens de até 200km e R$ 0,45 para viagens mais longas.

distancia = int(input('Digite a distância da viagem em quilometros: '))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45

print ('O preço da passagem é R$ {:.2f}'.format(passagem))