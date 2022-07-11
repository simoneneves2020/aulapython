while True:
    print("""

Menu
----
1 - Adição
2 - Subtração
3 - Divisão
4 - Multiplicação2
5 - Sair

""")
    opcao =int(input("Escolha uma opcao:"))
    if opcao== 5:
        break
    elif opcao >=1 and opcao <5:
        n = int(input("Tabuada de:"))
        x = 1
        while x<=10:
            if opcao == 1:
                print("%d + %d = %d" % (n, x, n + x))
            elif opcao == 2:
                print("%d - %d = %d" % (n, x, n - x))
            elif opcao == 3:
                print("%d / %d = %5.4f" % (n, x, n / x))
            elif opcao == 4:
                print("%d x %d = %d" % (n, x, n * x))
            x=x+1
    else:
        print("opcao invalida!")