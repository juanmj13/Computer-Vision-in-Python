import cv2
import numpy as np

# Cargar imagen
image = cv2.imread("red.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Rango de color (ejemplo: rojo)
lower_color = np.array([0, 100, 100])
upper_color = np.array([10, 255, 255])

# Crear máscara y aplicar
mask = cv2.inRange(hsv, lower_color, upper_color)
result = cv2.bitwise_and(image, image, mask=mask)

# Encontrar contornos del objeto
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 500:  # Filtrar ruido
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Objeto detectado", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
