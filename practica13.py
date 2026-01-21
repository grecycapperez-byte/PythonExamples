#lectura y escritura de archivos 
archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

#Escritura
"""Para escribir datos en un archivo, lo abrimos en modo de escritura ("w") utilizando la función open().
Si el archivo no existe, se creará automáticamente. Si el archivo ya existe, su contenido se sobrescribirá."""

archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()

#También puedes utilizar la declaración with para manejar la apertura y cierre de archivos de manera automática.
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
