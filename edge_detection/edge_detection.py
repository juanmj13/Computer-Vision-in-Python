import cv2
import os
from dotenv import load_dotenv
import matplotlib.pyplot as plt
import numpy as np

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

# Load the image in color
image = cv2.imread(image_path)

# Perform edge detection using the Canny algorithm
edges = cv2.Canny(image, lower_threshold, upper_threshold)

# Create a dilation kernel to control the thickness of the edges
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (border_thickness * 2 + 1, border_thickness * 2 + 1))

# Dilate and then Erode to separate neighborhoods
edges_dilated = cv2.dilate(edges, kernel)
edges_eroded = cv2.erode(edges_dilated, kernel)  # Erode to break small connections

# Find connected components to identify individual neighborhoods
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(edges_eroded)

# Get the areas of all components (excluding the background)
areas = stats[1:, cv2.CC_STAT_AREA]
largest_indices = np.argsort(areas)[-3:] + 1  # Get indices of the 3 largest components

# Create an output image to visualize the 3 largest neighborhoods
output_image = np.zeros_like(image)

# Draw the 3 largest neighborhoods and mark their centroids
for i, label in enumerate(largest_indices):
    mask = (labels == label)
    color = np.random.randint(0, 255, size=(3,), dtype=np.uint8)  # Random color for each neighborhood
    output_image[mask] = color

    # Get the centroid coordinates
    center_x, center_y = int(centroids[label][0]), int(centroids[label][1])

    # Draw an "X" at the centroid
    cv2.line(output_image, (center_x - 5, center_y - 5), (center_x + 5, center_y + 5), (0, 0, 255), 2)  # Diagonal line 1
    cv2.line(output_image, (center_x + 5, center_y - 5), (center_x - 5, center_y + 5), (0, 0, 255), 2)  # Diagonal line 2

# Show the original image and the image with neighborhoods and centroids
plt.figure(figsize=(10, 5))

# Show the original image
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert from BGR to RGB for matplotlib
plt.title('Original Image')
plt.axis('off')

# Show the image with neighborhoods and centroids
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))  # Convert from BGR to RGB for matplotlib
plt.title('Top 3 Neighborhoods with Centroids')
plt.axis('off')

# Display the images
plt.show()

# Save the output image with centroids marked
output_path = "top_3_neighborhoods_with_centroids.jpg"
cv2.imwrite(output_path, output_image)
print(f"Image with the 3 largest neighborhoods and centroids saved as {output_path}")
