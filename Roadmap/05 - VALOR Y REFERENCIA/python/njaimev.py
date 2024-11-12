# Pasar una variable por valor es cuando dentro de otra variable se le asigna el valor de otra variable, asi la variable original NO CAMBIA SU VALOR ORIGINAL.
# Se suele usar en tipos de datos inmutables: int, float, str, tuple.

# 1. Enteros:

x = 10
y = x
y = 5

print(x) # al imprimir x no cambia su valor, aunque se le asigna a y.
print(y)

# 2. Flotantes

float1 = 1.5
float2 = float1
float2 = 10.8

print(float1)
print(float2)

# 3. Cadenas

cad1 = "Hola"
cad2 = cad1
cad2 = "Adiós"

print(cad1)
print(cad2)

# 4. Tuple

tup1 = (1, 2, 3)
tup2 = tup1
tup2 = (3, 2, 1)

print(tup1)
print(tup2)

# En este caso al asignar una variable a otra variable y posteriormente cambiando el valor de la segunda variable, el valor de la primera variable no cambia.


# Asignar por referencia es cuando se asigna una variable a otra y usan la misma ubicación de memoria, cambiar una variable AFECTA A LA OTRA.
# Se usa en tipos de datos mutables: list, dict, set.


# 1. list

list1 = [1, 2, 3, 4]
list2 = list1
list2.append(5)

print(list1)
print(list2)

# 2. Dict

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = dict1
dict2["d"] = 4

print(dict1)
print(dict2)

# 3. Set

set1 = {1, 2, 3, 4}
set2 = set1
set2.add(5)

print(set1)
print(set2)

# En este caso cuando se le asigna una variable a otra, y se le quiere agregar un valor a la segunda, las dos variables son modificadas.
# Esto ocurre porque la variable no almacena directamente el valor de la otra variable, sino que guarda una referencia a la ubicación de ese objeto en la memoria.



# Una función en python siempre se le pasan variables por referencia.
# Dependiendo del valor (inmutable o mutable) se pasa la variable por valor o referencia.


#Con datos inmutables: por valor
def funcion(num):
    num = 10          # Se crea una variable dentro de una función.
    print("El numero es: ", num)

num2 = 5              # Se crea otra variable y se le pasa a la función.
funcion(num2)

print("Fuera de la función: ", num2) # El valor de num2 sigue siendo 5.

# Aunque un valor se pase como parámetro para una función, este seguira valiendo lo que se le asignó fuera de la función.
# Aqui parece que el valor fue "pasado por valor", ya que no afecta a la variable original.


#Con datos mutables: por referencia
def agregar(lista):
    lista.append(4)       # En caso de usar esta función, se agregará el 4 a la lista que se le pasa.
    print("Lista: ", lista)

mi_lista = [1, 2, 3]
agregar(mi_lista)
print("Fuera de la función: ", mi_lista)

# Cuando estos valores se pasan a una función, cualquier modificación al contenido de estos objetos van a afectar al objeto original.


# Si se quiere evitar la asignación por referencia se puede utilizar la función copy() para crear una copia INDEPENDIENTE del objeto.
# ejemplo: 
set1 = {1, 2, 3, 4}
set2 = set1.copy()
set2.add(5)

print(set1)
print(set2)

def mod_lista(lista):
    lista_mod = lista.copy()
    lista_mod.append(30)
    print("Dentro de la función: ", lista_mod)

my_list = [10, 20]
mod_lista(my_list)

print("Fuera de la función: ", my_list)

"""
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""
