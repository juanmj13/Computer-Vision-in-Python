import cv2
import numpy as np

def detectar_golpes(ruta_imagen, area_minima=45):
    # Cargar imagen
    imagen = cv2.imread(ruta_imagen)
    if imagen is None:
        print("No se pudo cargar la imagen.")
        return

    # Redimensionar si es muy grande (opcional)
    scale_percent = 35  # usa 100% del tamaño original
    width = int(imagen.shape[1] * scale_percent / 100)
    height = int(imagen.shape[0] * scale_percent / 100)
    imagen = cv2.resize(imagen, (width, height))

    # Mostrar original
    cv2.imshow("01 - Imagen original", imagen)

    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    cv2.imshow("02 - Escala de grises", gris)

    # Suavizado con filtro Gaussiano
    suavizada = cv2.GaussianBlur(gris, (5, 5), 0)
    cv2.imshow("03 - Desenfoque Gaussiano", suavizada)

    # Detección de bordes con Canny
    bordes = cv2.Canny(suavizada, 50, 150)
    cv2.imshow("04 - Canny (bordes)", bordes)

    # Encontrar contornos
    contornos, _ = cv2.findContours(bordes.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar bounding boxes
    imagen_salida = imagen.copy()
    area_img = imagen.shape[0] * imagen.shape[1]
    contornos_validos = 0

    for contorno in contornos:
        area = cv2.contourArea(contorno)
        x, y, w, h = cv2.boundingRect(contorno)
        area_bb = w * h
        porcentaje = area_bb / area_img

        cumple = area > area_minima and porcentaje < 0.5

        color = (0, 255, 0) if cumple else (0, 0, 255)  # Verde si cumple, rojo si no
        cv2.rectangle(imagen_salida, (x, y), (x + w, y + h), color, 2)

        texto = f"A:{int(area)} P:{porcentaje:.2f}"
        cv2.putText(imagen_salida, texto, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1, cv2.LINE_AA)

        if cumple:
            contornos_validos += 1

    cv2.imshow("05 - Daños detectados", imagen_salida)
    print(f"Se detectaron {contornos_validos} daños dentro del tamaño permitido (<50% del área).")

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Uso del script
ruta = r'C:\Users\Juan Manuel JC\Desktop\Experiment\l4.jpg'
detectar_golpes(ruta)
