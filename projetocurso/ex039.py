idade = int(input('Digite sua idaede:.. '))
if idade > 18:
    print('Você provavelmente se alistou a {} anos atrás... '.format(idade - 18))
elif idade < 18:
    print('Você precisa se alistar daqui a {} anos...'.format(18 - idade))
else:
    print('Você precisa se alistar esse ano... ')
