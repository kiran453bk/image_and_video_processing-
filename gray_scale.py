import cv2
import matplotlib.pyplot as plt

# Read an image
img = cv2.imread('C:/Users/Basavaraj Kulkarani/OneDrive/Desktop/DSC/image_and_video_processing-/pexels-sharad-7199194.jpg')  # OpenCV reads in BGR format

# Convert BGR to RGB for displaying
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display image
plt.imshow(img_rgb)
plt.title("My Image")
plt.show()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale Image")
plt.show()

# Resize
resized = cv2.resize(img, (200, 200))
