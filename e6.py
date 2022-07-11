print('=====DESAFIO 09=====')
print('\nFaça um programa que leia um número inteiro e mostre a sua tabuada.')
num = int(input('Digite um número:'))
counter = 0
tab = 2
while counter <= tab:
    res = num * counter
    print('{} * {} = {}'.format(num, counter, res))
    counter += 1