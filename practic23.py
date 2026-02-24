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
    print(f"No tienes descuento. Pagas: ${compra}")

#restaurante de comida rapida 
Pizza:10.00
Hamburguesa:8.00
Ensalada: 6.00
cliente = input("¿Qué comida deseas ordenar?")
if cliente.lower()  == "pizza":
    print("El precio de la Pizza es $10.00")
elif cliente.lower() == "hamburguesa":
    print("El precio de la Hamburguesa es $8.00")
elif cliente.lower() == "ensalada":
    print("El precio de la Ensalada es $6.00")
else: 
       print("Lo siento, no tenemos esa comida disponible.")



#La Hucha de Ahorros

#La Hucha de Ahorros
total_ahorros = 0
while True:
    ingreso = float(input("Ingrese el monto a ahorrar (o -1 para salir): "))
    if ingreso == -1:
        break
    total_ahorros += ingreso
    print(f"Total ahorrado hasta ahora: {total_ahorros:.2f}")
    if total_ahorros >= 500:
        print("¡Meta alcanzada! Has ahorrado 500 o más.")
        break

#La Lista de Invitados a tu Fiesta
#invitados 
invitados = []
while True:
     nombre = input("¿A quién quieres invitar? ")
     if nombre == "fin":
          break
     print(f"Nuevo invitado: {nombre}")
     invitados.append(nombre)
print("Lista de invitados:")
for invitado in invitados:
     print(invitado)        

     
