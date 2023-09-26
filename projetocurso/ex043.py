peso = float(input('Digite seu peso em kilos:.. '))
altura = float(input('Digite sua altura em métros:.. '))
imc = peso/(altura * altura)
print('Seu imc é {:.2f} '.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!!!')
elif 18.5 <= imc <= 25:
    print('Você está no peso ideal!!!')
elif 25 < imc < 30:
    print('Você está no sobrepeso!!!')
elif 30 <= imc < 40:
    print('Você está obeso kkkkkkk')
else:
    print('Você está na obesidade morta, um pé na cova ja')
