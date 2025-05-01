import cv2

# === Configuración ===
rtsp_url = 'rtsp://admin:AetoArch1@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'
sensitivity_threshold = 5  # Sensibilidad de 0 a 100 (porcentaje mínimo del frame con movimiento para dibujar BB)

# Conexión a la cámara
cap = cv2.VideoCapture(rtsp_url)
if not cap.isOpened():
    print("Error streaming video")
    exit()

# Inicializar primer frame
ret, prev_frame = cap.read()
if not ret:
    print("No se pudo leer el primer frame.")
    cap.release()
    exit()

# Redimensionar frame inicial
prev_frame = cv2.resize(prev_frame, (640, 480))
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
prev_gray = cv2.GaussianBlur(prev_gray, (21, 21), 0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error al leer el frame.")
        break

    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Calcular la diferencia absoluta entre el frame actual y el anterior
    frame_delta = cv2.absdiff(prev_gray, gray)
    thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    # Encontrar contornos del movimiento detectado
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

    # Actualizar el frame anterior
    prev_gray = gray.copy()

    # Salir con 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Limpiar recursos
cap.release()
cv2.destroyAllWindows()
