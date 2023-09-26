velocidade = float(input('Digite a velocidade do carro:.. '))
if velocidade > 80:
    print('Você foi mutado no valor de R${:.2f}!..'.format((velocidade - 80)*7))

else:
    print('Você não foi mutado...')
