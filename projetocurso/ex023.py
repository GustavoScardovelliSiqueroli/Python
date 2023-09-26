numero = int(input('Digite um número de 0 a 9999:.. '))
u = numero % 10
d = (numero // 10)% 10
c = (numero //100) %10
m = (numero //1000) % 10
print('Unidade:.. {}'.format(str(u)))
print('Dezena:.. {}'.format(str(d)))
print('Centena:.. {}'.format(str(c)))
print('Milhar:.. {}'.format(str(m)))
