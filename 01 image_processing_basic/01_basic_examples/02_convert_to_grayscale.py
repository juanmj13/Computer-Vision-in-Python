import cv2

image = cv2.imread("example.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Escala de Grises", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
