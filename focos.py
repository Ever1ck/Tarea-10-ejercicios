def NumeroFocos():
    Color = float()
    Verdes = float()
    Blancos = float()
    Rojos = float()
    n = float()

    print("Ingrese el valor de n:")
    n = float(input())

    for x in range(1,n+1):
        print("PROCESO ",x)
        print("Seleccione el valor de color.")
        print("1.- verde")
        print("2.- blanco")
        print("3.- rojo")
        while True:
            Color = float(input())
            if Color<1 or Color>3:
                print("Ingrese un numero valido")
            if Color>=1 and Color<=3: break
        if Color==1:
            Verdes = Verdes + 1
        if Color==2:
            Blancos = Blancos + 1
        if Color==3:
            Rojos = Rojos + 1
        print("")
	print("Valor de focos verdes: ",Verdes)
	print("Valor de focos blancos: ",Blancos)
	print("Valor de focos rojos: ",Rojos)