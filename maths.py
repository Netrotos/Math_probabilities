while True:

    menu = int(input("\n1 - Numero de subconjuntos\n2 - Arranjos com repeticao\n3 - Fatorial\n"))

    if menu == 1:
        num1 = int(input("#Conjunto\n"))
        r1 = 2 ** num1
        print("Numero de subconjuntos: " + str(r1))
    elif menu == 2:
        p = int(input("#Elementos\n"))
        n = int(input("#Conjunto (Possibilidades)\n"))
        r2 = n ** p
        print("Numero total: \n" + str(r2))
    elif menu == 3:
        def factorial(n):
            if n == 0:
                return 1
            else:
                return n * factorial(n - 1)
        
        n = int(input("Fatorial de : \n"))
        print("Factorial de " + str(n) + ": " + str(factorial(n)))


