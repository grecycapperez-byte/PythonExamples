#Tienes 3 calificaciones de un alumno: 8.5, 9.0 y 7.5. Debes calcular el promedio final.
Alum1=8.5
Alum2=9.0
Alum3=7.5
alumnos= (Alum1 + Alum2 + Alum3)/3 
print("El promedio final es:", alumnos)

alumno4=9.3
alumno5=8.7
alumno6=6.6
alumnos2= (alumno4 + alumno5 + alumno6)/3
print("Promedio del salon es:",alumnos2)

#Area y perimetro 
#Usar fórmulas matemáticas básicas ($Area = base \times altura$)
base= 20
altura=15
area= base * altura
perimetro= (2 * base)+(2 * altura)
print("El area es de:",area)
print("El perimetro es de:",perimetro)

bc=40
al=20
are= bc * al
perimtro= (2 * bc) + (2 * al)
print("El area es de:",are)
print("El perimetro es de:",perimtro)

#Entender la diferencia entre división normal / y división entera //.
mintotal = 130
hora = mintotal //60
minrest= mintotal % 60
print("Son",hora,"horas y", minrest, "minutos.")

minto = 500
hr = minto // 80
minrestante= minto % 80
print("Son",hr,"horas y ", minrestante,"minutos")

#Objetivo: Usar el operador de potencia **
peso= 58
altura= 1.56
masamus=peso/(altura **2)
print("Tu índice de masa corporal es:", masamus)

ps=76
alt= 1.98
masamos= ps /(alt **2)
print("EL indice de masa corporal es:",masamos)

#Ejercicio 5: Tu Calculadora de Edad

nacimi= int(input("¿En qué año naciste? "))
anacl = 2026
edad= anacl - nacimi
print("Al final del 2026 tnedras:",edad,"años.")

cuenta = float(input("¿De cuánto fue la cuenta? "))

propina = cuenta * 0.10
total_a_pagar = cuenta + propina

print("La propina es:", propina)
print("Debes pagar en total:", total_a_pagar)

edad= (int (input ("Ingresa tu edad")
if edad >= 18:
print("Bienvenido! Puedes pasar.")

else 
print("No puedes pasar aun eres menor de edad.")
print("Fin del programa.")

#Par o impar
numero =int (input ("Ingresa un numero entero"))
if numero %2==0
print (f"Es un {numero} numero par ")
else 
prinr (f"Es un {numero}numero impar")

#Calificaciones (Usando elif)
if nota >= 90
pritn("Excelente nota!")
elif nota >= 70 
pritn("Aprobado.")
else
print("Reprobado. Necesitas estudiar más.")

producto =float(input("Que precio tiene tu producto?"))
if precio > 1000 
nuevopre = precio *0.80
print(f"El nuevo precio con descuento es: {nuevopre}")
else 
print("No aplica descuento",precio)

#La Montaña Rusa
altura =float(input("Ingresa la altura: "))
edad =int(input("ingresa la edad: "))
if altura >1.40 and edad >10:
         print("Puedes subir!")
else:
          print("Lo siento, no cumples los requisitos")
#El Contador
for numero in range(11):
    multiplica = 5 * numero 
    print(multiplica) 
for num in range(200)
 multi = 6 * num 
         print(multi)
#: Mezclando todo (Bucle + If)
for num in range (1, 11):
 if num == 5:
  print("¡MITAD DEL CAMINO!")
else: 
    print(num)
 for edad in range (20,40)
if edad ==5
print("En camino de adulto!")

#Listas (Tu primera base de datos)
amigos = ["Ana", "Beto", "Carla"]
  print (amigos [0])
    print (amigos [2])
    amigos[1] = "Roberto"
amigos.append("Daniel")
print(amigos) 

tienda = ["Manzana", "Leche", "Pan"]
print (tienda [0])
 print(tienda [2])
tienda [2]="Cereal"
tienda.append("Huevos")
print(tienda)
print(len(tienda))  # Esto nos diría que hay 4 productos
