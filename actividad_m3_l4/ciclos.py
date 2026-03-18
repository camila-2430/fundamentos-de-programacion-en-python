    ## 1 uso basico de while

numero = 1 #inicio la variable

while numero <= 5:   #condicion
    print(numero)
    numero += 1  # incremento para evitar un bucle infinito

    ## 2 uso basico de for

frutas = ["manzana", "platano", "naranja"]

for fruta in frutas:
    print(fruta)

    ## 3 condicion en un ciclo

for numero in range(1, 11): # porque se cuenta desde 0

    if numero % 2 == 0:
        print(numero, "par")

    else:
        print(numero, "impar")

    ## 4 ciclo infinito controlado con break
"""
while True:  
    numero = int(input("ingresa un numero (0 para salir): "))

    if numero == 0:
        print("fin del programa")
        break
"""
        
    ## 5 ciclo anidado

for i in range(1, 4): 
    print("tabla del", i)

    for j in range(1, 11):
        print(i, "x", j,"=", i * j)

        print() #linea en blanco para que quede separado

    ## 6 uso de continue

# lista de nombres
lista_nombres = ["Megan", "Juan", "Mateo", "Thomas", "Juan", "Madelinne"]

# ciclo for que recorre cada nombre d ela lista

for nombre in lista_nombres:

    # si el nombre es juan se salta esta iteracion
    # continue hace que no se ejecute el print y pase al siguiente elemento
    if nombre == "Juan":
        continue

    #se imprime solo si el nombre NO es juan
    print(nombre)
