premax= 5000.0 
nombre="Vacaciiones en familia"
dinero_disponible = floa(inpunt("Con cuanto dinero cuentas realmente para este viaje?"))
gastos=[90.00,150.00,200.50] #comida, reguerdos, ospedaje 
nuevo_gasto = float(input("Introduce un gasto extra: "))
gastos.append(nuevo_gasto)
total_gastado=0
for g in gastos : 
  total_gastado = total_gastado + g
  print(f"Procesando gasto: ${g}")
  if total_gastado > premax
print("Cuidado! Te has pasado del presupuesto.")
diferencia= total_gastado - premax
print(f"Debes reducir tus gastos en: ${diferencia}")
elif total_gastado > (premax * 0.8):
print("Estas cerca del limite. Gasta con precaucion!")
else: 
print("Todo bien. Tu presupuesto esta bajo control.")
