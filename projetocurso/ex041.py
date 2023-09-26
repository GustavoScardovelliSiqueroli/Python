idade = int(input('Qual a idade do atleta?.. '))
if 0 < idade <= 9:
    print('Este atleta é mirim... ')
elif 9 < idade <= 14:
    print('Este atleta é infantil... ')
elif 14 < idade <= 19:
    print('Este atleta é junior...')
elif 19 < idade <= 20:
    print('Este atleta é sênior...')
else:
    print('Este atleta é master...')
