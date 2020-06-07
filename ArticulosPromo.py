def Descuento():

    Total = 0
    print("Ingrese el numero de productos")
    Art = int(input())

    for i in range(1, Art+1):
        print("Articulo",i)
        print("ingrese precio del articulo")
        Precio = int(input())
        Descuento = Precio*0.1
        if Precio >= 200:
            Descuento = Precio*0.15
        if Precio > 100 and Precio < 200:
            Descuento = Precio*0.12
        Costo = Precio - Descuento
        Total = Total+Costo
        print("Valor del Costo: ",Costo)
        print("Descuento es de: ",Descuento)
    print("Valor Total es de: ", Total)

Descuento()