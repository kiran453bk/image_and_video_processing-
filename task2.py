import cv2
import numpy as np

# Read Image
img = cv2.imread("C:/Users/Basavaraj Kulkarani/OneDrive/Desktop/DSC/image_and_video_processing-/Screenshot 2025-05-08 221206.png")  # Change filename
h, w, c = img.shape

# Mid points
mid_h, mid_w = h // 2, w // 2

# Create blank image
output = np.zeros_like(img)

# Split quadrants
Q1 = img[:mid_h, :mid_w]      # Top-left
Q2 = img[:mid_h, mid_w:]      # Top-right
Q3 = img[mid_h:, :mid_w]      # Bottom-left
Q4 = img[mid_h:, mid_w:]      # Bottom-right

# Make 1st quadrant Red only
R = Q1.copy()
R[:, :, 1] = 0      # remove G
R[:, :, 2] = 0      # remove B

# Make 2nd quadrant Green only
G = Q2.copy()
G[:, :, 0] = 0      # remove B
G[:, :, 2] = 0      # remove R

# Make 3rd quadrant Blue only
B = Q3.copy()
B[:, :, 1] = 0      # remove G
B[:, :, 2] = 0      # remove R

# 4th quadrant Original → Q4

# Place into output image
output[:mid_h, :mid_w] = R
output[:mid_h, mid_w:] = G
output[mid_h:, :mid_w] = B
output[mid_h:, mid_w:] = Q4

# Display
cv2.imshow("Quadrant Color Manipulation", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
