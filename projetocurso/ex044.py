preco = float(input('Digite o preco do produto que vc irá comprar:..'))
desconto = int(input('''
Digite o número do método de pagamento que desejar:::
1- À vista no dinheiro (10% de desconto);
2- À vista no cartão (5% de desconto);
3- Em até 2x no cartão (preço normal);
4- 3x ou mais no cartão (20% de juros);

Eu desejo:.. '''))
if desconto == 1:
    print('Você irá pagar R${:.2f}, com R${:.2f} em desconto'.format(preco - (preco/100*10), (preco/100*10)))
elif desconto == 2:
    print('Você irá pagar R${:.2f}, com R${:.2f} em desconto'.format(preco - (preco/100*5), (preco/100*5)))
elif desconto == 3:
    print('Você irá pagar R${:.2f} em duas vezes sem desconto'.format(preco))
else:
    print('Você irá pagar R${:.2f} com os 20% de juros'.format(preco + preco/100*20))
