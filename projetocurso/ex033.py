n1 = int(input('Digite um número'))
n2 = int(input('Digite outro número'))
n3 = int(input('Digite um terceiro número'))
primeiro = int()
segundo = int()
terceiro = int()
if n1 > n2:
    if n2 > n3:
        primeiro = n3
        segundo = n2
        terceiro = n1
    else:
        if n1 > n3:
            primeiro = n2
            segundo = n3
            terceiro = n1
        else:
            primeiro = n2
            segundo = n1
            terceiro = n3
else: #n2 maior que n1
    if n1 > n3:
        primeiro = n3
        segundo = n1
        terceiro = n2
    else:
        if n2 > n3:
            primeiro = n1
            segundo = n3
            terceiro = n2
        else: #n3 maior que n1 e n3 maior que n1
            primeiro = n1
            segundo = n2
            terceiro =n1

print('Sequencia arrumada com if else:.. {}, {}, {}.'.format(primeiro, segundo, terceiro))



