import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread(r"C:/Users/Basavaraj Kulkarani/OneDrive/Desktop/images/download.jpg")

if img is None:
    print("Image not found")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Normalize image to range [0,1]
    img_norm = img / 255.0

    # Gamma values
    gamma_values = [0.5, 1.0, 2.0]

    # Display
    plt.figure(figsize=(12,4))

    for i, gamma in enumerate(gamma_values):
        gamma_corrected = np.power(img_norm, gamma)

        plt.subplot(1, 3, i+1)
        plt.imshow(gamma_corrected)
        plt.title(f"Gamma = {gamma}")
        plt.axis("off")

    plt.tight_layout()
    plt.show()
