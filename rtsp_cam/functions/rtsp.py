import cv2
from onvif import ONVIFCamera
from urllib.parse import urlparse
import numpy as np
from datetime import datetime
import os


def liveCam(rtsp_url: str, width: int, height: int, user: str, password: str):
    # Insertar user:password en la URL RTSP
    parsed = urlparse(rtsp_url)

    if parsed.username is None and parsed.password is None:
        netloc = f"{user}:{password}@{parsed.hostname}"
        if parsed.port:
            netloc += f":{parsed.port}"
        rtsp_url = parsed._replace(netloc=netloc).geturl()

    cap = cv2.VideoCapture(rtsp_url)

    if not cap.isOpened():
        print("Error streaming video")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error in frame. Exit...")
            break

        frame_resized = cv2.resize(frame, (width, height))
        cv2.imshow('IP Cam - Live Stream', frame_resized)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('t'):
            TakePhoto(frame)

    cap.release()
    cv2.destroyAllWindows()


def discovery(ip: str, port: int, user: str, password: str) -> str:
    try:
        # Connect to the camera
        cam = ONVIFCamera(ip, port, user, password)

        # Create media service
        media_service = cam.create_media_service()

        # Get the first profile
        profiles = media_service.GetProfiles()
        token = profiles[0].token

        # Setup stream request
        stream_setup = media_service.create_type('GetStreamUri')
        stream_setup.StreamSetup = {
            'Stream': 'RTP-Unicast',
            'Transport': {'Protocol': 'RTSP'}
        }
        stream_setup.ProfileToken = token

        # Get stream URI
        uri = media_service.GetStreamUri(stream_setup)
        print(f"RTSP URL DISCOVERED:\n{uri.Uri}")
        return uri.Uri

    except Exception as e:
        print(f"Error discovering camera stream: {e}")
        return ""
    
def movementDetectionBasic(rtsp_url: str, width: int, height: int, user: str, password: str, sensitivity_threshold: float):
    # Insertar user:password en el RTSP URL si no viene incluido
    parsed = urlparse(rtsp_url)

    if parsed.username is None and parsed.password is None:
        netloc = f"{user}:{password}@{parsed.hostname}"
        if parsed.port:
            netloc += f":{parsed.port}"
        rtsp_url = parsed._replace(netloc=netloc).geturl()

    # Conexión a la cámara
    cap = cv2.VideoCapture(rtsp_url)
    if not cap.isOpened():
        print("Error streaming video")
        return

    # Leer el primer frame
    ret, prev_frame = cap.read()
    if not ret:
        print("No se pudo leer el primer frame.")
        cap.release()
        return

    prev_frame = cv2.resize(prev_frame, (width, height))
    prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
    prev_gray = cv2.GaussianBlur(prev_gray, (21, 21), 0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error al leer el frame.")
            break

        frame = cv2.resize(frame, (width, height))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        # Calcular diferencia entre frames
        frame_delta = cv2.absdiff(prev_gray, gray)
        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        frame_area = frame.shape[0] * frame.shape[1]

        for contour in contours:
            area = cv2.contourArea(contour)
            percent_area = (area / frame_area) * 100

            if percent_area >= sensitivity_threshold:
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, f"{percent_area:.1f}%", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        cv2.imshow("IP Cam - Movimiento", frame)

        prev_gray = gray.copy()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('t'):
            TakePhoto(frame)

    cap.release()
    cv2.destroyAllWindows()


def trackingColor(rtsp_url: str, width: int, height: int, user: str, password: str,
                  lower_hsv: tuple, upper_hsv: tuple, min_area: int = 500):
    # Insertar user:password en la URL si no está incluido
    parsed = urlparse(rtsp_url)
    if parsed.username is None and parsed.password is None:
        netloc = f"{user}:{password}@{parsed.hostname}"
        if parsed.port:
            netloc += f":{parsed.port}"
        rtsp_url = parsed._replace(netloc=netloc).geturl()

    # Conexión a la cámara
    cap = cv2.VideoCapture(rtsp_url)
    if not cap.isOpened():
        print("No se pudo abrir el stream de video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo recibir el frame (stream cortado?). Saliendo...")
            break

        frame_resized = cv2.resize(frame, (width, height))
        hsv = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2HSV)

        # Crear máscara basada en el color deseado
        mask = cv2.inRange(hsv, np.array(lower_hsv), np.array(upper_hsv))

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > min_area:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame_resized, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('Tracking de color', frame_resized)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if cv2.waitKey(1) & 0xFF == ord('t'):
            TakePhoto(frame)

    cap.release()
    cv2.destroyAllWindows()

def TakePhoto(frame, folder='photos'):
    """
    Guarda el frame actual como una imagen JPEG usando la fecha y hora actual en el nombre.

    Parámetros:
    - frame: Frame actual de la cámara (imagen).
    - folder: Carpeta donde guardar la foto. Por defecto 'photos'.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(folder, f"photo_{timestamp}.jpg")
    cv2.imwrite(filename, frame)
    print(f"[INFO] Foto guardada: {filename}")