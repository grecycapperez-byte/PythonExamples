#if y elif 
edad=int(input("Ingresa tu edad:"))
if edad >=18 :
     print ("Puedes pasar a ver la pelicula.")
else:
    print("Lo siento, necesitas ser mayor de edad.")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#El Probador de Números (Par o Impar)
num=int(input("Ingresa el numero del usuario:"))
if num % 2==0:
    print("Es un numero par")
else:
    print("Es numero impar")



# SIMULADOR DE LEYES ROBÓTICAS
orden = input("¿Qué orden le das al robot? ")
identidad = input("¿Quién da la orden? (humano/robot): ")

# El robot solo obedece a humanos
if identidad == "robot":
    print("No recibo órdenes de otros robots.")

# PRIMERA LEY: No dañar humanos
elif "golpear" in orden or "herir" in orden:
    print("ERROR: No puedo dañar a un humano. (1ra Ley)")

# SEGUNDA LEY: Obedecer órdenes (si no rompen la primera)
elif orden == "limpiar" or orden == "trabajar":
    print("ORDEN ACEPTADA: Empezando a " + orden)

# TERCERA LEY: Protección propia
elif orden == "salta al fuego":
    print("ERROR: Debo proteger mi existencia. (3ra Ley)")

else:
    print("No entiendo esa orden o no entra en mis protocolos.")


#Clasificador de temperaturas 
temp = float(input("¿A cuántos grados estamos? "))
if temp == 30:
   print("Hace mucha calor!")
elif temp >= 20:
       print("Aqui el clima esta perfecto!")
elif temp >=10:

     print("Está fresco, lleva suéter")
else:
       print("Hace mucho frío")

#El Examen de la Academia Jedi
color= input("¿Qué color de sable de luz prefieres?")
if color == "verde":
    print("Eres un Maestro como Yoda")
elif color == "azul":
    print("Eres un Caballero como Anakin")
elif color=="rojo":
    print("Te has unido al Lado Oscuro (Sith)")
else:
    print("Ese color no existe en la galaxia")

#Calculadora de Descuentos
compra=float(input("Monto total:"))
if compra >= 1000:
    descuento = compra * 0.20
    pago_total = compra - descuento
    print(f"¡Felicidades! Tienes un descuento de 20%. Pagas: ${pago_total}")
elif compra >=500:
    descuento = compra * 0.10
    pagototal = compra - descuento
    print(f"Felicidades tienes un descuento del 10%. Pagas: ${pagototal}")
else: 
    compra <= 500
    print(f"No tienes descuento. Pagas: ${compra}")
