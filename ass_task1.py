import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('C:/Users/Basavaraj Kulkarani/OneDrive/Desktop/images/Screenshot 2025-05-08 221242.png')

# Convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to binary (Thresholding)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display results using matplotlib
plt.figure(figsize=(12, 4))

# Original image (convert BGR to RGB for matplotlib)
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

# Gray scale image
plt.subplot(1, 3, 2)
plt.imshow(gray, cmap='gray')
plt.title("Gray Scale")
plt.axis("off")

# Binary image
plt.subplot(1, 3, 3)
plt.imshow(binary, cmap='gray')
plt.title("Binary Image")
plt.axis("off")

plt.show()