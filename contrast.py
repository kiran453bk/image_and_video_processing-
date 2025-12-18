import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread(r"C:/Users/Basavaraj Kulkarani/OneDrive/Desktop/images/download.jpg")

if img is None:
    print("Image not found")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Contrast variations
    low_contrast  = cv2.convertScaleAbs(img, alpha=0.5, beta=0)
    normal        = cv2.convertScaleAbs(img, alpha=1.0, beta=0)
    high_contrast = cv2.convertScaleAbs(img, alpha=2.0, beta=0)

    # Display
    plt.figure(figsize=(12,4))

    plt.subplot(1,3,1)
    plt.imshow(low_contrast)
    plt.title("Low Contrast (α=0.5)")
    plt.axis("off")

    plt.subplot(1,3,2)
    plt.imshow(normal)
    plt.title("Original / Normal Contrast")
    plt.axis("off")

    plt.subplot(1,3,3)
    plt.imshow(high_contrast)
    plt.title("High Contrast (α=2.0)")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
