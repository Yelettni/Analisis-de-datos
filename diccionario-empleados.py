# SISTEMA DE PAGO DE LA CONSTRUCCIÓN DE LA PIRÁMIDE:
# Salarios con bonificaciones y descuentos

print("Bienvenido al sistema de pago de la construcción de la pirámide de la sabiduría")

# Diccionario con información de los trabajadores
trabajadores = {
    "Juan": {"horas_trabajadas": 45, "tardanzas": 2},
    "Maria": {"horas_trabajadas": 38, "tardanzas": 4},
    "Pedro": {"horas_trabajadas": 50, "tardanzas": 1},
    "Ana": {"horas_trabajadas": 42, "tardanzas": 3},
    "Luis": {"horas_trabajadas": 40, "tardanzas": 0}
}

# Tarifa por hora
TARIFA_POR_HORA = float(input("Ingrese la tarifa por hora para los trabajadores: "))

# Recorrer el diccionario y calcular los pagos
for nombre, datos in trabajadores.items():
    horas_trabajadas = datos["horas_trabajadas"]
    llegadas_tarde = datos["tardanzas"]
    
    if horas_trabajadas > 40:
        horas_extras = horas_trabajadas - 40
        pago_normal = 40 * TARIFA_POR_HORA
        pago_extra = horas_extras * TARIFA_POR_HORA * 1.2
    else:
        pago_normal = horas_trabajadas * TARIFA_POR_HORA
        pago_extra = 0
    
    sueldo_bruto = pago_normal + pago_extra
    bonificacion = 50000 if sueldo_bruto > 600000 else 0
    descuento = sueldo_bruto * 0.05 if llegadas_tarde >= 3 else 0
    sueldo_neto = int(sueldo_bruto + bonificacion - descuento)
    
    print(f"\nSr/Sra. {nombre}, su sueldo bruto es de {sueldo_bruto} pesos")
    print(f"Bonificación: {bonificacion} pesos")
    print(f"Descuento por tardanzas: {descuento} pesos")
    print(f"Sueldo neto a pagar: {sueldo_neto} pesos\n")