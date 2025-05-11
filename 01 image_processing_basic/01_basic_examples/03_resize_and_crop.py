import cv2

image = cv2.imread("example.jpg")
resized = cv2.resize(image, (300, 300))
cropped = image[50:200, 100:300]

cv2.imshow("Redimensionada", resized)
cv2.imshow("Recorte", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
