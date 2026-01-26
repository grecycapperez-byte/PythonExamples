#podemos importar y utilizar estas funciones en nuestro programa principal.
import operaciones
import utilidades


resultado = operaciones.sumar(5, 3)
utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")


nombre = utilidades.obtener_nombre_usuario()
utilidades.imprimir_mensaje(f"Hola, {nombre}!")

#Atajos aritmeticos 
# Type your code below
count = 0
count =4
count*=2
count -=1
# Don't change the line below
print(f"count = {count}")

#matematicas simples 
# Type your code below
# Replace question marks with correct values
a = 4
b = 6

# Don't change the line below
c = b * a
print(f'c = {c}')
