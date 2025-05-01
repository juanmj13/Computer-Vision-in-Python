import cv2

# Discovered URL
rtsp_url = 'rtsp://admin:AetoArch1@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0&unicast=true&proto=Onvif'

# Create connection
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error streaming video")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error in frame. Exit...")
        break

    # Redimensionar el frame a un tamaño más pequeño (por ejemplo, 640x480)
    frame_resized = cv2.resize(frame, (640, 480))  # Cambia las dimensiones según sea necesario

    # Show the frame
    cv2.imshow('IP Cam - Live Stream', frame_resized)

    # Press 'q' for exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clear resources
cap.release()
cv2.destroyAllWindows()
