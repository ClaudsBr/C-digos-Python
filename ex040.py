# Media escolar informando se o aluno foi reprovado, se esta de recuperação ou se foi aprovado

nota1 = float(input('Digite sua nota da primeira avaliação: '))
nota2 = float(input('Digite sua nota da segunda avaliação: '))
trabalho = float(input('Digite sua nota de trabalho: '))

media = (((nota1+nota2)/2)*0.7)+ (trabalho * 0.3)
if media >= 7.0:
    print('\33[1;34mPARABÉNS\33[m, você obteve uma média de {:.1f} e está \33[4;34mAPROVADO!'.format(media))
elif media < 5.0:
    print('\33[0;31mInfelizmente sua média é de {:.1f} e você está\33[m \33[4;31mREPROVADO'.format(media))
else:
    print('\33[0;33mVocê obteve uma média de {:.1f} e está de\33[m \33[4;33mRECUPERAçÂO!'.format(media))