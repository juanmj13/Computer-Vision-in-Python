# Basic Examples

In this section you will find a serie of examples for learning basic image processing. 

## Prerequisites

For this section **01_basic_examples** ensure you have OpenCV and the following libraries intaled.  You can install it using pip:

```bash
pip install opencv-python
 ```

## Examples

### 01_load_and_show_image
This example will open a window with the example/jpg image in original size. 


```python
import cv2

image = cv2.imread("example.jpg")  # Make sure to have this image in the same directory

#### Display the image
cv2.imshow("Original Image", image)
cv2.waitKey(0)  # Wait for a key press to close the window
cv2.destroyAllWindows()  # Close the window after the key press
```

### 02_convert_to_grayscale
In this example, we load the image and use cv2.cvtColor() to convert the image from its original color format (BGR) to grayscale (cv2.COLOR_BGR2GRAY). After that, we display the grayscale image in a window titled "Escala de Grises". The window will stay open until a key is pressed.


```python
import cv2

image = cv2.imread("example.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Escala de Grises", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
```