# Edge Detection with Canny Algorithm

This project applies edge detection using the Canny algorithm to an image loaded from a file. The detected edges are highlighted in blue on the original image. The edge detection thresholds and the thickness of the edges can be adjusted using environment variables.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- Matplotlib
- python-dotenv

## Installation

1. Clone the repository or download the project files.
2. Install the necessary dependencies:

   ```bash
   pip install opencv-python matplotlib python-dotenv

3. Create a .env file in the root directory of the project and define the following environment variables:

    ```bash
    IMAGE_PATH=path_to_your_image.jpg
    LOWER_THRESHOLD=100  # Lower threshold for edge detection
    UPPER_THRESHOLD=200  # Upper threshold for edge detection
    BORDER_THICKNESS=1   # Thickness of the dilated edges

- __IMAGE_PATH:__ Path to the image you want to process.
- __LOWER_THRESHOLD:__ Lower threshold for the Canny algorithm (default: 100).
- __UPPER_THRESHOLD:__ Upper threshold for the Canny algorithm (default: 200).
- __BORDER_THICKNESS:__ Thickness of the dilated edges (default: 1).

## Usage

1. Make sure the image file is located in the directory specified by IMAGE_PATH.

2. Run the Python script:

    ```bash
    python edge_detection.py

3. The script will display two images:
    - The original image.
    - The image with edges highlighted in blue.

4. The image with the blue edges will be saved as edges_output_with_blue.jpg in the current directory.


