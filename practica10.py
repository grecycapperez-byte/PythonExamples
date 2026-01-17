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
