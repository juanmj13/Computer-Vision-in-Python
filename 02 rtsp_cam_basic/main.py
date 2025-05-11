from functions import timingPhoto
from dotenv import load_dotenv
import os

load_dotenv()

ip = os.getenv("CAMERA_IP")
port = int(os.getenv("CAMERA_PORT"))
user = os.getenv("CAMERA_USER")
password = os.getenv("CAMERA_PASSWORD")
interval = int(os.getenv("PHOTO_INTERVAL", 30))
output_dir = os.getenv("PHOTO_OUTPUT_DIR", "./photos")

from functions import discovery
rtsp_url = discovery(ip, port, user, password)

if rtsp_url:
    timingPhoto(rtsp_url, 640, 480, user, password, interval, output_dir)
