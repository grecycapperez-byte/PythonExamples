#Conjuntos 
"""Un conjunto es una estructura de datos mutable y no ordenada que permite almacenar una 
colección de elementos únicos. Los conjuntos se encierran entre llaves {} o se crean utilizando la función set()."""
frutas = {"manzana", "banana", "naranja"}


frutas.add("pera")
print(frutas)  # Imprime {"manzana", "banana", "naranja", "pera"}


frutas.remove("banana")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.discard("uva")
print(frutas)  # Imprime {"manzana", "naranja", "pera"}


frutas.clear()
print(frutas)  # Imprime set()
