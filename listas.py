#Colecciones
#listas
Fibonacci = [0,1,1,2,3,5,8,13,21]

#Encontrar un elemento de la lista
print(Fibonacci[3])

#len para contar los elementos de la lista
cant_num = len(Fibonacci)
print(cant_num)


#Añadir un elemento en una posición o índice determinado. insert(<index>, <obj>)
Fibonacci.insert(0,"inicio")

#acceder a los elementos de la lista (ciclo for)
#for l in Fibonacci:
    #print(l)

#Añadir un elemento al final de la lista. Metodo (append)
Fibonacci.append(55)

#Añadir un elemento en una posición o índice determinado. insert(<index>, <obj>)
#Fibonacci.insert(0,"inicio")

#modificar dato
#Fibonacci[0] = "0"

#eliminar elemento
#Fibonacci.remove("inicio")

#comprobar si un elemento està en lista
print (8 in Fibonacci)

#Contar número de veces que está un elemento.
print(Fibonacci.count(13))

print (Fibonacci)