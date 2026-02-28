#contraseña
contraseña= input("Ingrese la contraseña: ")
if len(contrseña) >= 8:
    print("Tu contraseña es muy corta.")
elif len (contraseña) >= 12:
    print("Tu contraseña es segura.")
else:    print("Tu contraseña es muy segura.")

#otra vercion 

password = input("Crea tu nueva contraseña: ")


if len(password) < 8:
    print("Error: La contraseña debe tener al menos 8 caracteres.")
elif not any(char.isdigit() for char in password):
    print("Casi... pero tu contraseña necesita al menos un número.")

else:
    print("¡Perfecto! Contraseña segura creada con éxito.")


gato= input("Encontrate a tu gato?")
if gato == "si"
print("Me alegra que lo allas encontrado!  :) ")
else:
print("Lo siento mucho por ti. :(")

#Adivina el numero 
import random
numero_secreto = random.randitn(1,10)
intento =0
print("He pensado un numero del 1 al 10! intenta adivinarlo.")
while intento != numero_secreto:
intento= int(input("Introcduce tu numero:"))
if intento < numero_secreto:
    print("NEL pastel. Inteta de nuevo!")
elif intento > numero_secreto:
    print("NEL paste te fuiste muy alto. Intenta de nuevo! ")
else:
    print("Esooo! Lo lograste")

print("Fin del juego.")


import random
chofer = random.randint(1, 20)
adivina = int(input("adivinare  el numero que piensas del 1 al 20: "))
if adivina == chofer:
    print("felicidades, has ganado el viaje")
else:
    print("lo siento, perdiste", chofer )





