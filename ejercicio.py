nombre = ()

while nombre != "salir":
    Nombre = input("Ingrese el nombre del trabajador o salir para terminar:")
    if nombre == "salir":
        break

    horas_trabajadas = float(input("Por favor, ingrese el numero de horas trabajadas: "))
    tarifa_por_hora = float(input("Por favor, ingrese la tarifa por hora: "))
    llegadas_tarde = int(input("Cuantas llegadas tarde registra el trabajador?"))
    
    #Si un trabajador labora mas de 40h, tiene recargo por hora de 120%
     
    if horas_trabajadas > 40:
        horas_extras = (horas_trabajadas - 40)
        salario = (40 * tarifa_por_hora)
        recargo = horas_extras (tarifa_por_hora * 1.2)
        #Si no trabaja mas de 40h, recibe salario a tarifa plena
    else:
        salario = (horas_trabajadas * tarifa_por_hora)
        recargo = 0
    
    sueldo_bruto = (salario + recargo)
    bonificacion = 0
    descuento = 0
    #Si el sueldo bruto supera 600.000 pesos, se otorga una bonificación de 50.000 pesos.
    if sueldo_bruto > 600000:
        bonificacion = 50000
    #Descuento por tardanzas - Si llegó tarde 3 veces o más, se le descuenta 5% del sueldo bruto.
    if llegadas_tarde >= 3:
        descuento = (sueldo_bruto * 0.05)
    
    sueldo_neto = int ((sueldo_bruto + bonificacion) - descuento)

    print(f"Sr/Sra. {nombre}, su sueldo bruto es de ${sueldo_bruto}")
    print(f"Su bonificación es de ${bonificacion}")
    print(f"Tiene un descuento por tardanzas de ${descuento}")
    print(f"Su sueldo neto a pagar es de ${sueldo_neto}")



