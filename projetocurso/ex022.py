nome = input('Digite seu nome completo:.. ').strip()
desp = nome.split()
primeiro = desp[0]
print(nome.upper())
print(nome.lower())
print('O nome completo, sem espaços, tem {} letras'.format(len(''.join(desp))))
print('O primeiro nome tem:.. {} letras'.format(len(primeiro)))
