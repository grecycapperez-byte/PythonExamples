#crear y utilizar páquetes 
"""Para crear un paquete, creamos un directorio con el nombre deseado
y agregamos un archivo especial llamado __init__.py dentro del directorio. 
Este archivo puede estar vacío o contener código de inicialización del paquete."""
mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
from mi_paquete import modulo1, modulo2


modulo1.funcion1()
modulo2.funcion2()
