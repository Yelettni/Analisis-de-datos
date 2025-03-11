#print ("¡Hello, world!")
#print (2)
#print (2.5)
#Para que nos sirven los tipo de datos
#print (10+15)
#print(int(10+15))
#print(float(10.5+15))

#Booleanos - comprobar se 5 es menor que 10
#print(5<10)

#Booleanos - comprobar si 7 es mayor que 15
#print(7>15)
#horas_que_trabajo = 10
#horas_que_duermo = 5
#print("Horas totales",horas_que_trabajo + horas_que_duermo)

#Paso 1: Imprimir "Mensaje de Bienvenida para el trabajador"
print ("Bienvenido al programa de pagos para la construcción de la piramide")
(Nombre_del_trabajador) = input("Ingrese el nombre del trabajador: ")

#Paso 2: Paso 2: Definir Variables
horas_trabajadas = float(input("Ingrese el numero de horas trabajadas: "))
tarifa_por_hora = float(input("Ingrese la tarifa por hora: "))

#Paso 3: Calcular el Pago Total
print(f"El Total por horas trabajadas para el trabajador {Nombre_del_trabajador} es de $:", horas_trabajadas * tarifa_por_hora)
