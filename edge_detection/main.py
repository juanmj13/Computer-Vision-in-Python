import cv2
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt

# Load environment variables from the .env file
load_dotenv()

# Get the image path from the environment variables
image_path = os.getenv('IMAGE_PATH')

# Get and parse environment variables
lower_threshold = int(os.getenv('LOWER_THRESHOLD', 100))  # Default value is 100 if not set
upper_threshold = int(os.getenv('UPPER_THRESHOLD', 200))  # Default value is 200 if not set
border_thickness = int(os.getenv('BORDER_THICKNESS', 1))  # Default value is 1 if not set

# Check if the image path is valid
if not os.path.exists(image_path):
    print("The image path is not valid. Please ensure the path is correct.")
    exit()

# Load the image in color (to draw on it in blue)
image = cv2.imread(image_path)

# Perform edge detection using the Canny algorithm with adjustable border thickness
edges = cv2.Canny(image, lower_threshold, upper_threshold)

# Create a dilation kernel to control the thickness of the edges
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (border_thickness * 2 + 1, border_thickness * 2 + 1))

# Dilate the edges to make them thicker
edges_dilated = cv2.dilate(edges, kernel)

# Convert the dilated edges to a 3-channel (BGR) image to draw in color
edges_colored = cv2.cvtColor(edges_dilated, cv2.COLOR_GRAY2BGR)

# Create a mask to apply to the original image
# The edges will be blue, so we modify the values in the corresponding channels
image_with_edges = image.copy()
image_with_edges[edges_dilated != 0] = [255, 0, 0]  # Blue in BGR format

# Show the original image and the image with blue edges
plt.figure(figsize=(10, 5))

# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert from BGR to RGB for matplotlib
plt.title('Original Image')
plt.axis('off')

# Show the image with blue edges
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(image_with_edges, cv2.COLOR_BGR2RGB))  # Convert from BGR to RGB for matplotlib
plt.title('Image with Blue Edges')
plt.axis('off')

# Display the images
plt.show()

# Save the image with blue edges
output_path = "edges_output_with_blue.jpg"
cv2.imwrite(output_path, image_with_edges)
print(f"Image with blue edges saved as {output_path}")
