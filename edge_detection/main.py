import cv2
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Obtener la ruta de la imagen desde las variables de entorno
image_path = os.getenv('IMAGE_PATH')

# Obtener y parsear las variables de entorno
lower_threshold = int(os.getenv('LOWER_THRESHOLD', 100))  # Valor por defecto 100 si no está configurado
upper_threshold = int(os.getenv('UPPER_THRESHOLD', 200))  # Valor por defecto 200 si no está configurado

# Verificar si la ruta de la imagen es válida
if not os.path.exists(image_path):
    print("La ruta de la imagen no es válida. Asegúrate de que la ruta esté correcta.")
    exit()

# Cargar la imagen
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convertimos la imagen a escala de grises



# Realizar el edge detection usando el algoritmo Canny
edges = cv2.Canny(image, lower_threshold, upper_threshold)

# Mostrar la imagen original y los bordes detectados
plt.figure(figsize=(10, 5))

# Mostrar la imagen original
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

# Mostrar la imagen con los bordes detectados
plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title('Bordes Detectados')
plt.axis('off')

# Mostrar las imágenes
plt.show()

# Guardar la imagen de los bordes detectados
output_path = "edges_output.jpg"
cv2.imwrite(output_path, edges)
print(f"Imagen de bordes guardada como {output_path}")
