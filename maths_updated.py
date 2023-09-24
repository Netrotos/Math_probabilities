def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)

while True:

    menu = int(input("\n1 - Arranjos com repeticao\n2 - Arranjos sem repeticao\n3 - Permutacoes\n4 - Numero de subconjuntos\n"))

    if menu == 4:
        num1 = int(input("Conjunto"))
        r1 = 2 ** num1
        print("Numero de subconjuntos: " + str(r1))


    elif menu == 1:
        p = int(input("n.º elementos: "))
        n = int(input("n.º conjunto: "))
        r2 = n ** p
        print("Arranjos completos: " + str(r2))


    elif menu == 3:
        n = int(input("n.º elementos: "))
        print("Permutacoes: " + str(factorial(n)))

    elif menu==2:
        p = int(input("n.º elementos: "))
        n = int(input("n.º conjunto: "))
    
        r2 = (factorial(n))/factorial(n-p)
        print("Arranjos simples: " + str(r2))

