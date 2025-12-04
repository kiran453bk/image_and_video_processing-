import cv2

# Read the image
img = cv2.imread('C:/Users/Basavaraj Kulkarani/OneDrive/Desktop/images/Screenshot 2025-05-08 221242.png')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to binary using thresholding
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Save or display results
cv2.imwrite('gray_image.jpg', gray)
cv2.imwrite('binary_image.jpg', binary)