import random
import time

print(20*'=-=')
time.sleep(0.5)
print('JOGO DA VELHA')
time.sleep(0.5)
print('Escolha uma das opções e espere o computador responder.')
time.sleep(0.5)
print()

jogador = int(input('''DIGITE O NÚMERO CORRESPONDENTE PARA:..
1- PEDRA
2- PAPEL
3- TESOURA

Sua escolha é:.. '''))
print()

computador = random.randint(1, 3)
print('Carregando...')
time.sleep(1)
print('Carregando..')
time.sleep(1)
print('Carregando.')
time.sleep(1)
print()

if jogador == 1 and computador == 1:
    print('O computador escolheu PEDRA!!')
    time.sleep(1)
    print('Empate.')
elif jogador == 1 and computador == 2:
    print('O computador escolheu PAPEL!!')
    time.sleep(1)
    print('O computador vence.')
elif jogador == 1 and computador == 3:
    print('O computador escolheu TESOURA!!')
    time.sleep(1)
    print('O jogador vence.')
elif jogador == 2 and computador == 1:
    print('O computador escolheu PEDRA!!')
    time.sleep(1)
    print('O jogador vence.')
elif jogador == 2 and computador == 2:
    print('O computador escolheu PAPEL!!')
    time.sleep(1)
    print('Empate.')
elif jogador == 2 and computador == 3:
    print('O computador escolheu TESOURA!!')
    time.sleep(1)
    print('O computador vence.')
elif jogador == 3 and computador == 1:
    print('O computador escolheu PEDRA!!')
    time.sleep(1)
    print('O computador vence.')
elif jogador == 3 and computador == 2:
    print('O computador escolheu PAPEL!!')
    time.sleep(1)
    print('O jogador vence.')
elif jogador == 3 and computador == 3:
    print('O computador escolheu TESOURA!!')
    time.sleep(1)
    print('Empate.')

print()
time.sleep(1)

print(20*'=-=')
print('FIM DE JOGO!!')

#FAZER UMA LISTA COM OS ITENS E RELACIONAR ELES COM OS NÚMEROS JOGADOS