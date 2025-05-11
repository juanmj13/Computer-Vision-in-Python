import cv2

# Cargar imagen en escala de grises
image = cv2.imread("coins.jpg", cv2.IMREAD_GRAYSCALE)

# Binarizar: fondo blanco, objetos oscuros
_, binary = cv2.threshold(image, 180, 255, cv2.THRESH_BINARY_INV)

# Encontrar contornos
contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Convertir a BGR para dibujar a color
output = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

min_area = 500  # área mínima en píxeles para considerar un objeto
count = 0

for i, cnt in enumerate(contours):
    area = cv2.contourArea(cnt)
    print(area)
    if area > min_area:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(output, f"{count+1}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        count += 1

print(f"Objetos contados (mayores a {min_area} px²): {count}")

cv2.imshow("Objetos contados", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
