import cv2

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

    # Mostrar el frame
    cv2.imshow('Camara IP - Stream en vivo', frame)

    # Presiona 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
