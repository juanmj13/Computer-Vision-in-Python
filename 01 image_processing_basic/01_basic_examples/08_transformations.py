import cv2
import numpy as np

image = cv2.imread("example.jpg")
(h, w) = image.shape[:2]

# Traslación
translation_matrix = np.float32([[1, 0, 50], [0, 1, 30]])
translated = cv2.warpAffine(image, translation_matrix, (w, h))

# Rotación
center = (w // 2, h // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(image, rotation_matrix, (w, h))

# Volteo horizontal
flipped = cv2.flip(image, 1)

cv2.imshow("Trasladada", translated)
cv2.imshow("Rotada", rotated)
cv2.imshow("Volteada", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()
