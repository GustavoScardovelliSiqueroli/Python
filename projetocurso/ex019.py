import random
print('Digite o nome dos alunos em sequencia:.. ')
nome1 = input()
nome2 = input()
nome3 = input()
nome4 = input()
lista = [nome1, nome2, nome3, nome4]
print('O aluno sorteado foi:.. {}'.format(lista[random.randint(0,3)]))

