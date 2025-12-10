import cv2

# Read the image
img = cv2.imread('C:/Users/Basavaraj Kulkarani/OneDrive/Desktop/images/Screenshot 2025-05-08 221242.png')   # Change filename!

# Convert to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to binary (Thresholding)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Display results
cv2.imshow("Original", img)
cv2.imshow("Gray Scale", gray)
cv2.imshow("Binary Image", binary)

cv2.waitKey(0)
cv2.destroyAllWindows()
