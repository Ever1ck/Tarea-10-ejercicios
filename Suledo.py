def SDTrabajadores():
    TrabajadoresN = int()
    NTrabajador = str()
    Htrabajador = int()
    SHtrabajador =float()
    Ssemanal = float()

    print("Ingrese el numero de trabajadores")
    TrabajadoresN = int(input())

    for x in range(1, TrabajadoresN+1):
        print("Trabajador",x)
        print("Ingrese el nombre del trabajador")
        NTrabajador = str(input())
        print("¿Cuantas horas trabajo?")
        Htrabajador = int(input())
        print("¿Cual es el sueldo por hora?")
        SHtrabajador =float(input())

        Ssemanal = Htrabajador*SHtrabajador
        Descuento=0
        if Ssemanal > 0 and Ssemanal <= 150:
            Descuento = Ssemanal*0.05
        if Ssemanal > 150 and Ssemanal <= 300:
            Descuento = Ssemanal*0.07
        if Ssemanal >300 and Ssemanal <= 450:
            Descuento = Ssemanal*0.09
        Ssemanal = Ssemanal-Descuento

        print("Nombre del trabajador: ", NTrabajador)
        print("Descuento: ", Descuento)
        print("Sueldo Semanal: ", Ssemanal)

SDTrabajadores()