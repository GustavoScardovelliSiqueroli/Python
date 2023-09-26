import emoji
import random
n1 = random.randint(1,3)
print('Eu pensei em algum número de 1 a 3, tente adivinha-lo...')
n2 = int(input(''))
if n1 == n2:
    print(emoji.emojize('Fdp :rage::fu:... o número era {}', language='alias').format(n1))
else:
    print(emoji.emojize('Você errrou :sunglasses::wink:... o número era {}', language='alias').format(n1))
