
##decision simple

edad = 32

if edad >= 18:
    print("Eres mayor de edad") 
else:
    print("Eres menor de edad")

## decisiones multiples con elif

calificacion = 6

if calificacion == 7:
    print("Excelente")
elif calificacion == 6:
    print("Muy bien")
elif calificacion == 5:
    print("Bien")
elif calificacion == 4:
    print("Suficiente")
else:
    print("Insuficiente")

##condiciones anidadas

numero = 10

if numero >= 0:
    if numero == 0:
        print ("es cero")
    else:
        print ("numero positivo")
else:
        print ("Numero negativo")


##condicion de borde

# Solicitar al usuario un número entero
numero_ingresado = 720

# Verificar si el número es exactamente uno de los límites permitidos
if numero_ingresado == 1 or numero_ingresado == 100:
    print("Estás en un límite permitido")

# Verificar si el número está dentro del rango pero no es un extremo
elif numero_ingresado > 1 and numero_ingresado < 100:
    print("Dentro del rango")

# Si no cumple ninguna de las condiciones anteriores, está fuera del rango
else:
    print("Fuera del rango")

