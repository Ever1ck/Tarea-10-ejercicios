def AprovadosYDesaprobados():
    NotaA = float()
    Alumnos = int()
    Apro = 0
    Desa = 0

    print("Ingrese el valor de calificacion aprobatoria:")
    NotaA = float(input())
    print("Inserte el numero de alumnos")
    Alumnos = int(input())
    for x in range(1,Alumnos+1):
        print("Alumno ",x)
        print("Ingrese la calificacion del alumno:")
        calificacion = int(input())
        if calificacion>=NotaA:
            Apro = Apro+1
        else:
            Desa = Desa+1
    print("Numero de Aprobados: ", Apro)
    print("Numero de Reprobados: ", Desa)
AprovadosYDesaprobados()