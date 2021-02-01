# CONVERSOR de bases (Binário, OCtal ou Hexadecimal)

num = int(input('Digite um número inteiro: '))
opcao = int(input('''Digite a base que se quer converter:
[1]- Converter para a base \33[1;32mBinária\33[m
[2] - Converter para a base \33[1;34mOctal\33[m
[3] - converter para a base \33[1;31mHexadecimal\33[m\n'''))
if opcao == 1:
    print('O valor \33[1;33m{}\33[m convertido para a base \33[4;32mBINÁRIA\33[m é igual a \33[1;33m{}\33[m '.format(num,bin(num)[2:]))
elif opcao == 2:
    print('O valor \33[1;33m{}\33[m convertido para a base \33[4;34mOCTAL\33[m será igual a \33[1;33m{}\33[m '.format(num,oct(num)[2:]))
elif opcao == 3:
    print('O valor \33[1;33m{}\33[m covertido para a base \33[4;31mHEXADECIMAL\33[m será igual a \33[1;33m{}\33[m '.format(num, hex(num)[2:]))
else:
    print('\33[1;31mOpção INVÁlIDA!!!')