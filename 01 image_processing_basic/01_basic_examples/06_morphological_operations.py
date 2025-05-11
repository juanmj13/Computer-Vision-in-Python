import cv2
import numpy as np

image = cv2.imread("lines.jpg", cv2.IMREAD_GRAYSCALE)
_, thresh = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5, 5), np.uint8)

dilation = cv2.dilate(thresh, kernel, iterations=1)
erosion = cv2.erode(thresh, kernel, iterations=1)

cv2.imshow("Original", image)
cv2.imshow("Dilatada", dilation)
cv2.imshow("Erosionada", erosion)
cv2.waitKey(0)
cv2.destroyAllWindows()
