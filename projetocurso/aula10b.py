n1 = int(input('Digite sua primeira nota:.. '))
n2 = int(input('Digite sua segunda nota:.. '))
media = (n1 + n2)/2
if media > 6:
    print('Você passou de ano com a nota {}'.format(media))
else:
    print('Você reprovou, pois sua nota é {} e ela é menor do que 6'.format(media))
