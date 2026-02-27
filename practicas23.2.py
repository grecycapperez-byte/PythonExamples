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
