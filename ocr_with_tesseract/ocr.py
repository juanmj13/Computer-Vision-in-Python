import cv2
import pytesseract
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Get the image path from the environment variables
image_path = os.getenv('IMAGE_PATH')

# Path to the Tesseract executable (adjust according to your system)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows
# pytesseract.pytesseract_cmd = "/usr/bin/tesseract"  # Linux/Mac

def recognize_text(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Convert to grayscale (improves OCR accuracy)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply OCR to extract text and positions
    custom_config = r'--oem 3 --psm 3'  # Configuration to improve OCR
    data = pytesseract.image_to_data(gray, config=custom_config, output_type=pytesseract.Output.DICT)

    # Draw bounding boxes around detected text
    for i in range(len(data["text"])):
        if int(data["conf"][i]) > 50:  # Filter results with high confidence
            x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
            text = data["text"][i]
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the image with detected text
    cv2.imshow("OCR Result", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run the function with the defined image
recognize_text(image_path)
