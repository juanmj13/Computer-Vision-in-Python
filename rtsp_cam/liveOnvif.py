from onvif import ONVIFCamera
import keyboard
import time

# Configura tus datos
ip = '192.168.1.108'      # IP de tu cámara
port = 80                 # Puerto HTTP (normalmente 80)
user = 'admin'            # Tu usuario
password = 'AetoArch1' # Tu contraseña

# Conectar
cam = ONVIFCamera(ip, port, user, password)

# Obtener servicios
ptz = cam.create_ptz_service()
media_service = cam.create_media_service()
profile = media_service.GetProfiles()[0]  # Primer perfil disponible

# Crear una solicitud de movimiento
request = ptz.create_type('ContinuousMove')
request.ProfileToken = profile.token

# Función para mover
def move(x, y, zoom=0):
    request.Velocity = {
        'PanTilt': {'x': x, 'y': y},
        'Zoom': {'x': zoom}
    }
    ptz.ContinuousMove(request)
    time.sleep(0.2)  # Mover por un pequeño tiempo
    ptz.Stop({'ProfileToken': profile.token})  # Parar el movimiento

print("Control de cámara con flechas. Presiona 'Esc' para salir.")

while True:
    if keyboard.is_pressed('up'):
        move(0, 0.5)      # Mover arriba
    elif keyboard.is_pressed('down'):
        move(0, -0.5)     # Mover abajo
    elif keyboard.is_pressed('left'):
        move(-0.5, 0)     # Mover a la izquierda
    elif keyboard.is_pressed('right'):
        move(0.5, 0)      # Mover a la derecha
    elif keyboard.is_pressed('page up'):
        move(0, 0, 0.5)   # Zoom In
    elif keyboard.is_pressed('page down'):
        move(0, 0, -0.5)  # Zoom Out
    elif keyboard.is_pressed('esc'):
        print("Saliendo...")
        break
    time.sleep(0.05)
