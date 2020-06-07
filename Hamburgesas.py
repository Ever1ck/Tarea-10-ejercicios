def NaufragoSatisfecho():
    HSensillas = float()
    HDobles = float()
    HTriples = float()
    CostoS = float()
    CostoD = float()
    CostoT = float()
    tarjeta = float()
    MontoTotal = float()
    MontoSTarjeta = float()
    Eleccion = str()

    print("¿Cuantas hamburguesas sencillas quiere?")
    HSensillas = float(input())
    print("¿Cuantas hamburguesas dobles quiere?")
    HDobles = float(input())
    print("¿Cuantas hamburguesas triples quiere?")
    HTriples = float(input())

    CostoS = 20
    CostoD = 25
    CostoT = 28
    tarjeta = 0.05

    MontoSTarjeta = (HSensillas*CostoS)+(HDobles*CostoD)+(HTriples*CostoT)
    MontoTotal = MontoSTarjeta+(MontoSTarjeta*tarjeta)

    print("El monto actual es de: ",MontoSTarjeta, "¿Desea pagar con tarjeta? Se le cobrara un 5% mas")
    print("Escriba `S` si quieres pagar con tajeta y `N` sino quiere pagar con tarjeta")
    Eleccion = str(input()).upper()
    
    if Eleccion == "S":
        print("El monto total es: ",MontoTotal)
    if Eleccion == "N":
        print("El monto Total es: ", MontoSTarjeta)

    print("Gracias por la compra.")
NaufragoSatisfecho()