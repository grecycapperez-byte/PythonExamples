presumax = 500.0
nomviaje= "Vacaciones 2027"
dinero_disponible = float(input("¿Cuánto dinero tienes para este viaje? "))
gastos = [120.50, 45.0, 80.0] # Hotel, Comida, Souvenirs
nuegasto = float(input("Introduce un gasto extra (ej. transporte): "))
gastos.append(nuevo_gasto)
total_gastado = 0  

for g in gastos:
    total_gastado = total_gastado + g
    print(f"Procesando gasto: ${g}")
