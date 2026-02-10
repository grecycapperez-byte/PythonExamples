import time
from datetime import datetime

def registrar_ingreso():
    contador = 0
    archivo_log = "registro_uso.txt"
    
    print("--- Monitor de Actividad Iniciado ---")
    print("Presiona 'Enter' cada vez que 'entres' al celular (o Ctrl+C para salir)")

    try:
        while True:
            # Simulamos la detección de desbloqueo
            input("Esperando desbloqueo...") 
            
            contador += 1
            ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"Ingreso #{contador} detectado a las: {ahora}"
            
            # Guardar en el archivo
            with open(archivo_log, "a") as f:
                f.write(log_entry + "\n")
            
            print(f"✅ Registrado: {log_entry}")
            print("-" * 30)
            
    except KeyboardInterrupt:
        print(f"\n\nResumen: Registraste {contador} ingresos hoy.")
        print(f"Los detalles se guardaron en '{archivo_log}'.")

if __name__ == "__main__":
    registrar_ingreso()
