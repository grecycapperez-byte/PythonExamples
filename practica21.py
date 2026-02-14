def revisar_presupuesto(lista_gastos, limite):
    # Paso A: Sumamos los gastos
    total = sum(lista_gastos) # sum() es una función de Python que suma listas rápido
    
    # Paso B: Calculamos la diferencia
    balance = limite - total
    
    # Paso C: Devolvemos el resultado
    return balance

# --- AQUÍ EMPIEZA EL PROGRAMA PRINCIPAL ---

mi_limite = 1000
mis_gastos = [200, 150, 500]

# Llamamos a la función y guardamos el resultado en 'resultado'
resultado = revisar_presupuesto(mis_gastos, mi_limite)

if resultado > 0:
    print(f"Te sobran ${resultado}")
else:
    print(f"Te faltan ${abs(resultado)}") # abs() convierte números negativos a positivos





viaje_paris = revisar_presupuesto([100, 200, 50], 500)
viaje_tokio = revisar_presupuesto([500, 800], 1000)
viaje_mexico = revisar_presupuesto([50, 20, 30], 200)

print(f"Balance París: {viaje_paris}")
print(f"Balance Tokio: {viaje_tokio}")
