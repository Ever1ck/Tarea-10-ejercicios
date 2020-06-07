def IncrementoSueldo():
    Salario = float()
    Incremento = float()
    NAños = float()
    Años = ()

    print("¿Cuanto es el salario inicial?")
    Salario = float(input())
    print("¿Cuantos años esta trabajando?")
    Años = float(input())

    Incremento = 0.10
    NAños = 1

    while NAños<=Años:
        Salario = Salario+(Salario*Incremento)
        print("El salario en el año ", NAños," es de ",Salario)
        NAños = NAños+1
IncrementoSueldo()