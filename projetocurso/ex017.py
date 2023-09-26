import math
cateto1 = float(input('Digite o cateto adjacente do trinagulo:.. '))
cateto2 = float(input('Digite o cateto oposto do tringulo:.. '))
hipotenusa = math.hypot(cateto1, cateto2)
print('A hipotenusa de seu triângulo é:.. {}'.format(hipotenusa))
