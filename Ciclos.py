#Condicionales
    #if
#temperatura = 20
#if temperatura > 20:
        #print ("Hace calor")
#else:
        #print ("Hace frio")

#if, elif , else
#temperatura = 20
#if temperatura > 20:
        #print ("Hace calor")
#elif temperatura == 20:
        #print("El clima está fresco") 
#else:
        #print ("Hace frio")

#ciclo for
#for numero in range(1,11):
        #print ("subiendo el escalón:", numero)


#ciclo for con break
#word = "Python"
#for variable in word:
    #if variable == "h":
        #break
    #print(variable)

#ciclo while
caramelos = 10
while caramelos > 0:
    print("Me como un caramelo! 🍬..")
    caramelos = caramelos - 1
    if caramelos == 0:
     print ("Ya no quedan caramelos! 😢")
