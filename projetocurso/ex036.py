print(20* '=0=')
print('Seja bem vindo ao empréstimo bancário!..')
print(20* '=0=')
casa = float(input('Digite aqui o valor da casa que deseja comprar:.. '))
parcelas = int(input('Em quantos anos deseja pagar essa casa?.. '))
salario = float(input('Digite seu salário mensalmente:.. '))
valorM = casa/(parcelas*12)

if (salario * 3/10) >= valorM:
    print('Empréstimo aceito, o valor mensal fica para: {:.2f}'.format(valorM))
else:
    print('Empréstimo negado, o valor mensal ultrapassa 30% de seu salário!')
