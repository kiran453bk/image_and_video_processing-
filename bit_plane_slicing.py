import cv2
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Step 1: Read image and convert to grayscale
# -------------------------------------------------
img = cv2.imread(r"C:/Users/Basavaraj Kulkarani/OneDrive/Desktop/images/download.jpg")

if img is None:
    print("Image not found")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# -------------------------------------------------
# Step 2: Bit Plane Decomposition
# -------------------------------------------------
bit_planes = []
for i in range(8):
    bit_plane = (gray >> i) & 1
    bit_planes.append(bit_plane)

# -------------------------------------------------
# Step 3: Display Bit Planes
# -------------------------------------------------
plt.figure(figsize=(12,6))
for i in range(8):
    plt.subplot(2,4,i+1)
    plt.imshow(bit_planes[i], cmap='gray')
    plt.title(f"Bit Plane {i}")
    plt.axis("off")

plt.suptitle("Bit Plane Decomposition", fontsize=14)
plt.tight_layout()
plt.show()

# -------------------------------------------------
# Step 4: Reconstruct using ALL bit planes
# -------------------------------------------------
reconstructed_all = np.zeros_like(gray)
for i in range(8):
    reconstructed_all += bit_planes[i] * (2**i)

# -------------------------------------------------
# Step 5: Reconstruct using only MSB planes (5–7)
# -------------------------------------------------
reconstructed_msb = np.zeros_like(gray)
for i in range(5,8):
    reconstructed_msb += bit_planes[i] * (2**i)

# -------------------------------------------------
# Step 6: Display Reconstruction Results
# -------------------------------------------------
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(gray, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(reconstructed_all, cmap='gray')
plt.title("Reconstructed (All 8 Bit Planes)")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(reconstructed_msb, cmap='gray')
plt.title("Reconstructed (MSB Bit Planes 5–7)")
plt.axis("off")

plt.tight_layout()
plt.show()
