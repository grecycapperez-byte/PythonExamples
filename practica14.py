#Para importar modulos 
"""Para utilizar un módulo 
en nuestro programa, 
debemos importarlo utilizando 
la declaración import. Podemos importar un módulo 
completo o funciones específicas de un módulo."""
import math
resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

"""También podemos importar funciones específicas 
de un módulo utilizando la sintaxis
from módulo import función."""
from math import sqrt
resultado = sqrt(25)
print(resultado)  # Imprime 5.0

"""Permite trabajar con fechas y horas,
como datetime.now() (fecha y hora actual), 
datetime.date() (fecha), datetime.time() (hora), entre otras."""
import random
import datetime
numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10


fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual


