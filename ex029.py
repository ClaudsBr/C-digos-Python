# Programa que lê a velocidade de uma carro. Se ele ultrapassar 80 km/h, será mostrada uma mensagem dizendo que ele
# foi multado. A multa vai custar R$ 7,00 por cada Km acima do limite.

vel = int(input('Digite sua velocidade em Km/h: '))

if vel > 80:
    print('Você está MULTADO!')
    multa = (vel - 80) * 7
    print('Você deverá R$ {},00 de multa'.format(multa))
