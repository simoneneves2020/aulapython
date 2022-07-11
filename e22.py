print('Leia 3 notas e calcular a média.\n')
repeticoes = 3
for contador in range(repeticoes):
    n1 = float(input('Nota 1:'))
    n2 = float(input('Nota 2:'))
    n3 = float(input('Nota 3:'))
    media = (n1 + n2 + n3)/3

    print('Média:', media)
    if (media<=5.0):
        print('Reprovado')
    elif (media>=7.0):
        print('Aprovado')
    else:
        print('Recuperação')
