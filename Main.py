import numpy as np
import matplotlib.pyplot as plt

# Load an image using NumPy
image = plt.imread('C:path/to/image/image.png')

# Display the original image
plt.subplot(1, 2, 1)
plt.imshow(image)
plt.title('Original Image')

# Convert the image to grayscale
grayscale_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

# Apply a threshold to the grayscale image
threshold = 0.5
binary_image = np.where(grayscale_image > threshold, 1.0, 0.0)

# Display the binary image
plt.subplot(1, 2, 2)
plt.imshow(binary_image, cmap='gray')
plt.title('Binary Image')

# Show the plots
plt.tight_layout()
plt.show()
