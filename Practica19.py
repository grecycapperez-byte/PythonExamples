
# REPASO GENERAL DE FUNDAMENTOS DE PYTHON
# Autor: Dulce Grecia Pérez Capilla 

print(" 1. VARIABLES Y MÓDULO ")

a, b, c = 9, 2, 11
d = a % 2   
e = b % 3   
f = c % 10  

print(f"Valores de módulo calculados: d={d}, e={e}, f={f}\n")

print("--- 2. ENTRADA DE DATOS Y MATEMÁTICAS ---")
# Pedir datos y convertir tipos (float e int)
nombre = input("¿Cómo te llamas? ")
peso = float(input("Introduce tu peso en kg (ej: 70.5): "))
altura = float(input("Introduce tu altura en metros (ej: 1.75): "))

# Cálculo de IMC: peso / altura al cuadrado
imc = peso / (altura ** 2)
print(f"Hola {nombre}, tu IMC es de: {imc:.2f}")

# Decisión lógica (if/elif/else)
if imc < 18.5:
    print("Estado: Bajo peso")
elif imc >= 18.5 and imc < 25:
    print("Estado: Peso saludable")
else:
    print("Estado: Sobrepeso")
print("\n")

print("--- 3. MANIPULACIÓN DE LISTAS ---")
tienda = ["Manzana", "Leche", "Pan"]
print(f"Lista inicial: {tienda}")

# Modificar un elemento
tienda[2] = "Cereal" 
# Agregar un elemento
tienda.append("Huevos")
print(f"Lista actualizada: {tienda}")
print(f"Cantidad de productos: {len(tienda)}\n")

print("--- 4. BUCLES Y ACUMULADORES ---")
precios = [1.50, 3.20, 4.00, 2.10]
total = 0

# Recorrer la lista y sumar
print("Escaneando productos...")
for p in precios:
    total += p  
    print(f"Sumando precio: ${p}")

print(f"\nSubtotal: ${total:.2f}")


if total > 10:
    descuento = total * 0.10
    total_final = total - descuento
    print(f"¡Cupón aplicado! Descuento del 10%: -${descuento:.2f}")
    print(f"TOTAL A PAGAR: ${total_final:.2f}")
else:
    print(f"TOTAL A PAGAR: ${total:.2f}")
    print("No alcanzaste el mínimo para descuento.")

print("Fin del programa de fundamentos")
     
