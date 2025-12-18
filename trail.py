import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread(r"C:/Users/Basavaraj Kulkarani/OneDrive/Desktop/images/download.jpg")

if img is None:
    print("Image not found. Check the path.")
else:
    # Convert BGR to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Resize image (2x) using Nearest Neighbor
    resized_img = cv2.resize(
        img_rgb,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_NEAREST
    )

    # Plot side-by-side
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img_rgb)
    plt.axis("off")
    plt.title("Original Image")

    plt.subplot(1, 2, 2)
    plt.imshow(resized_img)
    plt.axis("off")
    plt.title("Resized Image (2x - Nearest Neighbor)")

    plt.tight_layout()
    plt.show()
