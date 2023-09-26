ano = int(input('Digite um ano:.. '))
calc = ano % 4
if calc == 0:
    print('o ano {} é bissexto...' .format(ano))
else:
    print(('o ano {} não é bissexto...'.format(ano)))