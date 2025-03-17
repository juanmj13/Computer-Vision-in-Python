# OCR Text Recognition with Tesseract and OpenCV for plate Detection

This project uses Python, Tesseract OCR, and OpenCV to detect and extract text from an image, displaying the results with bounding boxes.

## Requirements

Make sure you have the following installed:

- Python 3.x
- OpenCV (`cv2`)
- Tesseract OCR
- `pytesseract` library
- `python-dotenv` library

## Installation

1. **Install dependencies**:

   ```sh
   pip install opencv-python pytesseract python-dotenv
   ```

2. Install Tesseract OCR: 
Windows: Download here https://github.com/UB-Mannheim/tesseract/wiki
Linux (Ubuntu):

3. Set up the .env file: Create a .env file in the project root and specify the image path:

    ```sh
   pip IMAGE_PATH=path/to/your/image.jpg
    ```
4. Update the Tesseract path in the script:

    ```sh
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    ```

## Usage
Run the script:

    ```sh
    python ocr.py
    ```

## Configuration
You can modify the OCR behavior by changing the Tesseract config in the script. In this case, the parameters will be optimazed for car plates:

    ```sh
    custom_config = r'--oem 3 --psm 3'
    ```

- __oem 3:__ OCR Engine Mode (default LSTM)
- __psm 3:__ Page segmentation mode (default auto)

For more options, check the Tesseract documentation.



