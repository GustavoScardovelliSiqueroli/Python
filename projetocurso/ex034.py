salario = float(input('Digite seu salário:.. '))
aumento = float(0)
if salario > 1250:
    aumento = 0.1
else:
    aumento = 0.15
print('Seu novo salário é de:.. {}'.format(salario + salario * aumento))