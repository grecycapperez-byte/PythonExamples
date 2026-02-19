premax= 5000.0 
nombre="Vacaciiones en familia"
dinero_disponible = float(input("Con cuanto dinero cuentas realmente para este viaje?"))
gastos=[90.00,150.00,200.50] #comida, reguerdos, ospedaje 
nuevo_gasto = float(input("Introduce un gasto extra: "))
gastos.append(nuevo_gasto)
total_gastado=0
for g in gastos:
    total_gastado = total_gastado + g
    print(f"Procesando gasto: ${g}")
    if total_gastado >  premax:
        print("Cuidado! Te has pasado del presupuesto.")
    elif total_gastado > (premax * 0.8):
        print("Estas cerca del limite. Gasta con precaucion!")
    else:
        print("Todo bien. Tu presupuesto esta bajo control.")

diferencia = total_gastado - premax
print(f"Debes reducir tus gastos en: ${diferencia}")

#Utilizamos funciones 
def revisar_presupuesto(lista_gastos,limite):
    total = sum(lista_gastos)
    balance = limite -total 
return balance 

mi_limite = 1000
mis_gastos =[200,150 ,500]
resultado = revisar_presupuesto(mis_gastos, mi_limite)
if resultado > 0:
    print(f"Te sobran ${resultado}")
else: 
    print(f"Te faltan ${abs(resultado)}")
#tres viajes distintos.
viaje_paris = revisar_presupuesto([100, 200, 50], 500)
viaje_tokio = revisar_presupuesto([500, 800], 1000)
viaje_mexico = revisar_presupuesto([50, 20, 30], 200)

print(f"Balance París: {viaje_paris}")
print(f"Balance Tokio: {viaje_tokio}")

#Calculadora de IVA
def calcular_total_del_viaje (precio,descuento):
    precio_con_descuento= precio - descuento
    impuesto =precio_con_descuento * 0.16
    total = precio_con_descueto + impuesto 
    return total
    precio_original= float(input ("Ingresa el precio:"))
    desc = float(input("Ingresa el monto a descontar: "))
precio_final = calcular_total_del_viaje (precio_original,desc)
print (f"El precio total con IVA es de: ${precio_final:.2}")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Bucle while
respuesta = ""
while respuesta != "salir":
    respuesta = input("Escribe algo (o 'salir' para terminar): ")


def calcular_total_con_iva(lista_precios):
    subtotal= sum(lista_precios)
    total = subtotal * 1.16
    return total 
    productos = []
    escaneo= True 
    print("BIENVENIDO A LA SUPER TIENDA ")
    print("(Escribe 'cobrar' cuando hayas terminado)")

while escaneando:
    entrada= input("Escanea el precio del producto:")

if entrada.lower()== "cobrar":
    escaneando = False 
else: 
    precio = float(entrada)
    productos.append (precio)
    print(f"Producto de {precio} añadido.")

if len(productos) > 0:
    pago_final = calcular_total_con_iva(productos)
    print("\n" + "=" *20)
    print(f"Has comprado{Len(productos)}productos.")
    print(f"TOTAL A PAGAR (IVA incluido):${pago_final:.2}")
    print("="*20)
else:
    print("No compraste nada hoy. Vuelve printo!")


--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#El variador de contraseñas 
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

#semaforo inteligente 
color=int(input("Igresa un color del semaforo"))
elif  Verde 
pritn("Avanza!")
else:
pritn("Color no valido")
elif amarillo
print("precaucion!")
elif rojo
print("detente")

