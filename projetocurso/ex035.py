reta1 = float(input('Digite a medida da primeira reta'))
reta2 = float(input('Digite a medida da segunda reta'))
reta3 = float(input('Digite a medida da terceira reta'))
maior = float()

if reta1 > reta2:
    if reta1 > reta3:
        maior = reta1
    else:
        maior = reta3
else:
    if reta2 > reta3:
        maior = reta2
    else:
        maior = reta3

