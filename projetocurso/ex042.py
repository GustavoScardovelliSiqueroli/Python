reta1 = float(input('Digite a primeira reta:.. '))
reta2 = float(input('Digite a segunda reta:.. '))
reta3 = float(input('Digite a terceira reta:.. '))
if reta1 == reta2 == reta3:
    print('Este retângulo é equilátero...')
elif (reta1 == reta2) or (reta3 == reta1) or (reta2 == reta3):
    print('Este retângulo é isóceles...')
else:
    print('Este retângulo é escaleno...')
