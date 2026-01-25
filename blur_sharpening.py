import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread(r"C:/Users/Basavaraj Kulkarani/OneDrive/Desktop/images/download.jpg")

if img is None:
    print("Image not found")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # ---------- BLURRING ----------
    avg_blur = cv2.blur(img, (5,5))                 # Averaging filter
    gaussian_blur = cv2.GaussianBlur(img, (5,5), 0) # Gaussian filter

    # ---------- SHARPENING ----------
    sharpen_kernel = np.array([[ 0, -1,  0],
                               [-1,  5, -1],
                               [ 0, -1,  0]])
    sharpened = cv2.filter2D(img, -1, sharpen_kernel)

    # Display results
    plt.figure(figsize=(12,8))

    plt.subplot(2,2,1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(2,2,2)
    plt.imshow(avg_blur)
    plt.title("Averaging Blur (5x5)")
    plt.axis("off")

    plt.subplot(2,2,3)
    plt.imshow(gaussian_blur)
    plt.title("Gaussian Blur (5x5)")
    plt.axis("off")

    plt.subplot(2,2,4)
    plt.imshow(sharpened)
    plt.title("Sharpened Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
