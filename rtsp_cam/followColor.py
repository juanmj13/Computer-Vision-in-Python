import cv2
import numpy as np

# Tu URL RTSP descubierta
rtsp_url = 'rtsp://admin:AetoArch1@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'

# Abrir la conexión de video
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("No se pudo abrir el stream de video.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo recibir el frame (stream cortado?). Saliendo...")
        break

    # Redimensionar el frame a un tamaño más pequeño (por ejemplo, 640x480)
    frame_resized = cv2.resize(frame, (640, 480))  # Cambia las dimensiones según sea necesario

    # Convertir el frame a HSV
    hsv = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2HSV)

    # Definir el rango de color amarillo en HSV
    lower_yellow = np.array([20, 100, 100])  # Valor mínimo para amarillo
    upper_yellow = np.array([30, 255, 255])  # Valor máximo para amarillo

    # Crear una máscara que solo contenga los colores amarillos
    mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Encontrar los contornos en la máscara
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar el bounding box alrededor del objeto amarillo
    for contour in contours:
        if cv2.contourArea(contour) > 500:  # Ignorar contornos pequeños
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame_resized, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Rectángulo verde

    # Mostrar el frame con el bounding box
    cv2.imshow('Camara IP - Stream en vivo con Bounding Box', frame_resized)

    # Presiona 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
