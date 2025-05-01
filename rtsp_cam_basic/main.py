from functions import discovery, liveCam, movementDetectionBasic, trackingColor
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Parámetros de la cámara desde .env
ip = os.getenv("CAMERA_IP")
port = int(os.getenv("CAMERA_PORT"))
user = os.getenv("CAMERA_USER")
password = os.getenv("CAMERA_PASSWORD")

# Obtener RTSP URL
rtsp_url = discovery(ip, port, user, password)

# Amarillo en HSV
lower_yellow = (20, 100, 100)
upper_yellow = (30, 255, 255)


if rtsp_url:
    liveCam(rtsp_url, 640, 480, user, password)
    # movementDetectionBasic(rtsp_url, 640, 480, user, password, 5)
    # trackingColor(rtsp_url, 640, 480, user, password, lower_yellow, upper_yellow)
