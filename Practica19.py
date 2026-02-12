#Actividad de ejemlo
import time
from datetime import datetime

def registrar_ingreso():
    contador = 0
    archivo_log = "registro_uso.txt"
    
    print("--- Monitor de Actividad Iniciado ---")
    print("Presiona 'Enter' cada vez que 'entres' al celular (o Ctrl+C para salir)")

    try:
        while True:
            input("Esperando desbloqueo...") 
            
            contador += 1
            ahora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"Ingreso #{contador} detectado a las: {ahora}"
        
     
