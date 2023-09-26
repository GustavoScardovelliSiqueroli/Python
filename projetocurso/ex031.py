distancia = float(input('Digite a distância que irá percorrer em sua viagem:.. '))
valor = 0
if  distancia < 200:
    valor = 0.50
else:
    valor = 0.45
print('O valor total da viagem percorrida é de R${:.2f}'.format(distancia * valor))