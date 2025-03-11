#Diccionario

#agenda ={
    #"Ana": "3005362098",
   # "Luis": "3148763456",
    #"Jorge": "3025769834"
#}

#modificar
#agenda["Ana"] = 3214356789

#eliminar elementos
#del agenda["Ana"]

#recorrer un dic..
#for key, value in agenda.items():
    #print (key,value)

# Diccionario 
Ingredientes_torta = {
    "harina":"420gr",
    "azúcar":"600gr",
    "cacao en polvo":"1½ tazas",
    "Margarina":"350gr",
    "huevos":"4 und",
    "polvo de hornear":"1 cucharadita",
    "leche":"480 mililitros",
    "esencia de vainilla":"2 cucharaditas"
 }

for key, value in Ingredientes_torta.items():
    print(key,value)

for ingrediente in Ingredientes_torta.items():
    print(*ingrediente,sep=' ')
    

