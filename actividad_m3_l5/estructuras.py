# creando estructuras


mi_lista = ["mango", "piña", "sandia"]

mi_tupla = (10, 20, 30)

mi_conjunto = {1.5, 2.5, 3.5}

mi_diccionario = {
    "nombre": "python",
    "version": 3.12,
    "tipo": "interpretado"
}

print("lista:", mi_lista)
#diferencia: ordenada y mutable

print("tupla:", mi_tupla)
#diferencia: ordenada pero inmutable

print("conjunto:", mi_conjunto)
#diferencia: no tiene orden y no permite elementos duplicados

print("diccinario:", mi_diccionario)
#diferencia: almacena pares clave-valor en lugar de elementos sueltos



    # 2 acceder a elementos

#segundo elemnto de la lista indice 1 
print(f"segundo elemento de la lista: {mi_lista[1]}")

#clave y valor del diccionario
print(f"clave: 'nombre' - valor: {mi_diccionario['nombre']}")

#los sets son colecciones desordenadas y al no tener un orden definido
#  o una posicion fija, python no puede usar indices como [0] o [1] 
# para localizar un elemento especfico.



    #contar e iterar

print(f"Largo de lista: {len(mi_lista)}")
print(f"Largo de tupla: {len(mi_tupla)}")
print(f"Largo de conjunto: {len(mi_conjunto)}")
print(f"Largo de diccionario: {len(mi_diccionario)}")


for elemento in mi_lista:
    print(f"Lista item: {elemento}")

for numero in mi_tupla:
    print(f"Tupla item: {numero}")

for decimal in mi_conjunto:
    print(f"Set item: {decimal}")

for clave, valor in mi_diccionario.items():
    print(f"Diccionario: {clave} -> {valor}")


    #4 modificar estructuras

# Modificar lista y conjunto
mi_lista.append("Damasco")
mi_conjunto.add(4.5)

# Borrar elemento de la lista
mi_lista.pop(0) # Borra el primero ("mango")

# Agregar clave al diccionario
mi_diccionario["creador"] = "camila osorio"

# Intentar modificar la tupla

try:
    mi_tupla[0] = 100
except TypeError as e:
    print(f"Error al modificar tupla: {e}")
    # Comentario: Las tuplas son inmutables. Una vez creadas, 
    # no permiten asignación de nuevos valores ni cambio de tamaño.

print(f"Lista final: {mi_lista}")
print(f"Set final: {mi_conjunto}")
print(f"Dict final: {mi_diccionario}")