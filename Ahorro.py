def AhorroPesos():
    Anual =0.01
    x = float()
    for x in range(1,366):
        print("Dia ",x)
        Anual = Anual*3
        Diario = Anual
        print("Valor ahorrado hasta hoy: ",Diario)
    print("Valor del Año: ",Anual)
AhorroPesos()