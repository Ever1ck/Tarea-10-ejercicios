def CuboNumeros():
    while True:
        print("Ingrese el valor de un numero")
        Numero = float(input())
        cubo = Numero*Numero*Numero
        print("Valor de cubo: ",cubo)
        while True:
            print("¿Desea repetir el proceso? (S/N):")
            tecla_repetir = input()
            if tecla_repetir=="s" or tecla_repetir=="n" or tecla_repetir=="S" or tecla_repetir=="N": break
        if tecla_repetir=="n" or tecla_repetir=="N": break
CuboNumeros()