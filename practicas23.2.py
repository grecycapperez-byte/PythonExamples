#contraseña
contraseña= input("Ingrese la contraseña: ")
if len(contrseña) >= 8:
    print("Tu contraseña es muy corta.")
elif len (contraseña) >= 12:
    print("Tu contraseña es segura.")
else:    print("Tu contraseña es muy segura.")
