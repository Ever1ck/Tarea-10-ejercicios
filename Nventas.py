def VentasTotales():
    Ventas = int()
    V0A10000 = 0
    V10000A20000 = 0
    MV0A1000 = 0
    MV10000A20000 = 0
    MontoTotal = 0

    print("Ingrese el numero de ventas")
    Ventas =int(input())
    for x in range(1, Ventas+1):
        print("Venta: ",x)
        print("Ingrese el valor")
        venta =float(input())
        if venta<=10000:
            V0A10000 = V0A10000+1
            MV0A1000 = MV0A1000+venta
        if venta>10000 and venta<=20000:
            V10000A20000 = V10000A20000+1
            MV10000A20000 = MV10000A20000+venta
        MontoTotal = MontoTotal+venta
        print("Valor de ventas de 0 a 10000: ", V0A10000)
    print("Valor de ventas de 10000 a 20000: ", V10000A20000)
    print("Valor de monto ventas de 0 a 10000: ", MV0A1000)
    print("Valor de monto ventas de 10000 a 20000: ", MV10000A20000)
    print("Valor de monto global: ", MontoTotal)
VentasTotales()