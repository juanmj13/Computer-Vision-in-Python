from onvif import ONVIFCamera

# Configuración
ip = '192.168.1.108'      # <-- Cambia por la IP de tu cámara
port = 80                # Puerto HTTP normal
user = 'admin'           # Tu usuario
password = 'AetoArch1'  # Tu contraseña

try:
    # Conectar a la cámara
    cam = ONVIFCamera(ip, port, user, password)
    
    # Crear servicio de Media
    media_service = cam.create_media_service()

    # Obtener el primer perfil
    profiles = media_service.GetProfiles()
    token = profiles[0].token

    # Crear correctamente el objeto de solicitud
    stream_setup = media_service.create_type('GetStreamUri')
    stream_setup.StreamSetup = {
        'Stream': 'RTP-Unicast',
        'Transport': {'Protocol': 'RTSP'}
    }
    stream_setup.ProfileToken = token

    # Ahora sí pedir la URL
    uri = media_service.GetStreamUri(stream_setup)
    
    print(f"RTSP URL descubierta:\n{uri.Uri}")

except Exception as e:
    print(f"Error: {e}")
