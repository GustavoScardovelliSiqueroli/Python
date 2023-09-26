frase = input('Digite uma frase qualquer:.. ').strip()
print('Quantas vezes aparece a letra "a" nessa frase?.. {}'.format(frase.upper().count('A')))
print('Posição que aparece pela primeira vez... {}'.format(frase.upper().find('A')))
print('A ultima vez que encontramos o "a" na frase foi na posição:.. {}'.format(frase.upper().rfind('A')))
