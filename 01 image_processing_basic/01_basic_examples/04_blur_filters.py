import cv2

image = cv2.imread("example.jpg")
blur = cv2.blur(image, (5, 5))
gaussian = cv2.GaussianBlur(image, (5, 5), 0)
median = cv2.medianBlur(image, 5)

cv2.imshow("Blur", blur)
cv2.imshow("Gaussian", gaussian)
cv2.imshow("Median", median)
cv2.waitKey(0)
cv2.destroyAllWindows()
