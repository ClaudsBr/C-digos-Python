# Alistamenteo Militar
# Maiores de 18 devem se alistar
# Menores de 18 retorna o tempo que falta para que eles se alistem


ano = int(input('Digite seu ano de nascimento: '))
idade = 2021 - ano
tempo = 0
if idade == 18:
    print('\33[1;34mJá está na hora de você se alistar!\33[m')
elif idade < 18:
    tempo = 18 - idade
    print('\33[1;32mVocê deverá se alistar daqui a {} ano(s)\33[m'.format(tempo))
else:
    tempo = idade - 18
    print('\33[1;31mVocê já passou do tempo de alistamento. Deveria ja ter se alistado há {} ano(s).\33[m'.format(tempo))

