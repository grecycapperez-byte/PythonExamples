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
def calcular_iva (precio):
    impuesto =precio * 0.16
    total = precio + impuesto 
    return total
    precio_usuario= float(input ("Ingresa el precio:"))
precio_final = calcular_iva (precio_usuario)
print (f"El precio total con IVA es de: ${precio_final:.2}")
    
