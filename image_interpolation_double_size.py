import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread(r"C:/Users/Basavaraj Kulkarani/OneDrive/Desktop/images/download.jpg")

if img is None:
    print("Image not found. Check the path.")
else:
    # Convert BGR to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Original dimensions
    h, w = img.shape[:2]

    # New dimensions (double size)
    new_size = (2 * w, 2 * h)

    # Interpolations
    nearest = cv2.resize(img, new_size, interpolation=cv2.INTER_NEAREST)
    bilinear = cv2.resize(img, new_size, interpolation=cv2.INTER_LINEAR)
    bicubic = cv2.resize(img, new_size, interpolation=cv2.INTER_CUBIC)

    # Display results
    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.imshow(nearest)
    plt.title("Nearest Neighbor")
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.imshow(bilinear)
    plt.title("Bilinear Interpolation")
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.imshow(bicubic)
    plt.title("Bicubic Interpolation")
    plt.axis("off")

    plt.tight_layout()
    plt.show()
