import pyrealsense2 as rs
import time
from dotenv import load_dotenv
import os
from datetime import datetime
import sys  # Necesario para el flush

# Cargar variables desde el archivo .env
load_dotenv()

# Obtener el intervalo de revisión desde el archivo .env
INTERVALO_REVISION = int(os.getenv("INTERVALO_REVISION", 5))  # Valor por defecto: 5 segundos

def obtener_numeros_serie():
    """Obtiene e imprime los números de serie de las cámaras Intel RealSense conectadas."""
    contexto = rs.context()
    dispositivos = contexto.query_devices()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if dispositivos.size() == 0:
        mensaje = f"{timestamp} - No hay cámaras Intel RealSense conectadas."
        print(mensaje)
        sys.stdout.flush()  # Forzar el flush para asegurarse que el mensaje se imprima
    else:
        for i, dispositivo in enumerate(dispositivos):
            numero_serie = dispositivo.get_info(rs.camera_info.serial_number)
            mensaje = f"{timestamp} - Cámara {i + 1}: Número de serie: {numero_serie}"
            print(mensaje)
            sys.stdout.flush()  # Forzar el flush para asegurarse que el mensaje se imprima

def iniciar_revision():
    """Revisa las cámaras cada cierto tiempo."""
    while True:
        obtener_numeros_serie()
        time.sleep(INTERVALO_REVISION)

if __name__ == "__main__":
    try:
        iniciar_revision()
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.stdout.flush()  # Asegúrate de que este error también se imprima inmediatamente
