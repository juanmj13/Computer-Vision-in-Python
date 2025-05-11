import cv2

# Cargar clasificador Haar preentrenado para detección de rostros
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Cargar imagen
image = cv2.imread("people.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar rostros
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))

# Dibujar rectángulos
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

print(f"Rostros detectados: {len(faces)}")

cv2.imshow("Detección de rostros", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
