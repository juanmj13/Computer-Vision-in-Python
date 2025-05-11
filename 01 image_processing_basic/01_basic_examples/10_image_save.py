import cv2

image = cv2.imread("example.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("imagen_gris.jpg", gray)
print("Imagen guardada como imagen_gris.jpg")
