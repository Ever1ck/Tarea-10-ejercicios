def ContarNnumeros():
    n = int()
    G = int()
    contador0 = int()
    contadormenor = int()
    contadormayor = int()
    total = int()

    print("Cuantos nuemeros desea ingresar")
    total = int(input())

    G = 1
    for G in range(1,total+1):
        print("Dame un numero")
        n = int(input())

        if n == 0:
            contador0 = contador0 +1
        if n < 0:
            contadormenor = contadormenor + 1
        if n > 0:
            contadormayor = contadormayor + 1

    print("La cantidad de ceros son:", contador0)
    print("la cantidad de numeros menores a cero son: ", contadormenor)
    print(" La cantidad de numeros mayores a cero son: ", contadormayor)
ContarNnumeros()