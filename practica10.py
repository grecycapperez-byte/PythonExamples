#Funciones definidas por el usuario 
#Ejemplo: funcion para calcular lamedia
def calcular_media (*numeros):
 suma = sum(numeros)
cantidad =len(numeros )
media = suma / cantidad 
return media 

print("Media:", calcular_media(10,20,30))
def sumar_3 (x):
 return x + 3
  
sumar = lambda x: x + 3
print("Sumar 3 a un número:", sumar (5))

"""Funciones con número variable de argumentos
Python permite definir funciones que acepten un número variable de argumentos.
Esto se logra utilizando el operador * antes del nombre del parámetro."""

def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22
