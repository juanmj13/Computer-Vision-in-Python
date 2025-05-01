from functions import discovery, liveCam, movementDetectionBasic, trackingColor

# Parámetros de la cámara
ip = '192.168.1.108'
port = 80
user = 'admin'
password = 'AetoArch1'

# Obtener RTSP URL
rtsp_url = discovery(ip, port, user, password)

# Amarillo en HSV
lower_yellow = (20, 100, 100)
upper_yellow = (30, 255, 255)

# Si obtuvimos un URL válido, mostrar el video
if rtsp_url:
    liveCam(rtsp_url, 640, 480, user, password)
    #movementDetectionBasic(rtsp_url,640,480,user,password,5)
    #trackingColor(rtsp_url, 640, 480, user, password, lower_yellow, upper_yellow)
    
