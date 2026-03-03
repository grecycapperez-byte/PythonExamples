#if y elif 
edad=int(input("Ingresa tu edad:"))
if edad >=18 :
     print ("Puedes pasar a ver la pelicula.")
else:
    print("Lo siento, necesitas ser mayor de edad.")

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

     


import random
numero_secreto = random.randint(1, 10)
intento = 0

print("¡He pensado un número del 1 al 10! Intenta adivinarlo.")
while intento != numero_secreto:
    intento = int(input("Introduce tu número: "))
    
    if intento < numero_secreto:
        print("Demasiado bajo. ¡Intenta otra vez!")
    elif intento > numero_secreto:
        print("Muy alto. Prueba de nuevo.")
    else:
        print("¡Exacto! Lo lograste.")

print("Fin del juego.")

#Modificacion de random 
import random

numero_secreto = random.randint(1, 20) 
energia = 5 

print(" JUEGO DE SUPERVIVENCIA NUMÉRICA ")
print("Adivina el número del 1 al 20. Tienes 5 puntos de energía.")

while energia > 0:
    intento = int(input(f"\nEnergía actual ({energia}): Introduce tu número: "))
    
    if intento == numero_secreto:
        print("¡Increíble! Has recuperado tu libertad. Ganaste.")
        break
    else:
        energia = energia - 1
        if intento < numero_secreto:
            print("Pista: El número es más alto.")
        else:
            print("Pista: El número es más bajo.")
            
        if energia == 0:
            print(f"Te has quedado sin energía. El número era {numero_secreto}. GAME OVER.")





pin_correcto = "1234"
intentos_restantes = 3

while intentos_restantes > 0:
    print(f"Tienes {intentos_restantes} intentos.")
    password = input("Introduce tu PIN de 4 dígitos: ")
    
    if password == pin_correcto:
        print("Acceso concedido. Bienvenido a tu cuenta.")
        break  
    else:
        intentos_restantes = intentos_restantes - 1
        print("PIN incorrecto.")

if intentos_restantes == 0:
    print("Tarjeta bloqueada por seguridad.")



#Modificacion 
saldo = 1000
pin_secreto = "1234"
acceso = False

intento_pin = input("Ingrese su PIN para comenzar: ")
if intento_pin == pin_secreto:
    acceso = True
    print("Acceso correcto.")
else:
    print("PIN incorrecto. Saliendo...")

while acceso == True:
    print("MENÚ BANCARIO ")
    print("1. Consultar saldo")
    print("2. Retirar dinero")
    print("3. Salir")
    
    opcion = input("Selecciona una opción (1-3): ")
    
    if opcion == "1":
        print(f"Tu saldo actual es de: ${saldo}")
    elif opcion == "2":
        retiro = int(input("¿Cuánto deseas retirar?: "))
        if retiro <= saldo:
            saldo = saldo - retiro
            print(f"Retiro exitoso. Nuevo saldo: ${saldo}")
        else:
            print("Error: Fondos insuficientes.")
    elif opcion == "3":
        print("Gracias por usar nuestro cajero. ¡Adiós!")
        break 
    else:
        print("Opción no válida, intenta de nuevo.")
