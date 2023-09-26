
numero = int(input('Digite um número inteiro qualquer para ser convertido:.. '))
convertido = int()
resto = str()
dividido = int()
print(30 * '.+.')
base = int(input('''Escolha a base para a conversão
1 - Binário
2 - Octal
3 - Hexadecimal 
:.. '''))
if base == 1:
    dividido = numero // 2
    resto = resto + str(numero % 2)
    print(dividido)
    print(resto)
#nao vou acabar isso pq ainda nao estou usando while.