diasGasto = int(input('Por quantos dias o carro foi alugado?.. '))
kmGastos = float(input('Quantos km o carro rodou nesse tempo?.. '))
print('O total a pagar será de R${:.2f}'.format(diasGasto*60 + kmGastos * 0.15))
