import cv2

# Cargar imagen
image = cv2.imread("example.jpg")  # Asegúrate de tener esta imagen en el mismo directorio

# Mostrar imagen
cv2.imshow("Imagen Original", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
