import cv2

image = cv2.imread("example.jpg")
cv2.rectangle(image, (50, 50), (200, 200), (0, 255, 0), 2)
cv2.circle(image, (300, 300), 50, (255, 0, 0), -1)
cv2.line(image, (0, 0), (400, 400), (0, 0, 255), 3)
cv2.putText(image, "Hola OpenCV", (50, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

cv2.imshow("Formas y Texto", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
