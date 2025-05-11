import cv2
import numpy as np


##Este codigo solo se basa en el numero de lados


# Cargar imagen
image = cv2.imread("shapes2.webp")  
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Invertir umbral para detectar formas negras sobre fondo blanco
_, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)

# Encontrar contornos
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    epsilon = 0.02 * cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    x, y, w, h = cv2.boundingRect(approx)

    shape = "Desconocido"
    sides = len(approx)

    if sides == 3:
        shape = "Triángulo"
    elif sides == 4:
        aspect_ratio = float(w) / h
        shape = "Cuadrado" if 0.95 < aspect_ratio < 1.05 else "Rectángulo"
    elif sides == 5:
        shape = "Pentágono"
    elif sides > 5:
        shape = "Círculo"

    cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)
    cv2.putText(image, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

cv2.imshow("Detección de formas", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
