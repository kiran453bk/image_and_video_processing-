

## 🔹 What is contrast variation?

Contrast variation means **changing the difference between dark and bright pixel values** in an image.

* **Low contrast** → image looks dull / washed out
* **High contrast** → dark regions darker, bright regions brighter

---

## ✅ Method used (simple & standard)

We use **linear contrast stretching**:

[
\text{New Image} = \alpha \times \text{Original Image} + \beta
]

* **α (alpha)** → contrast control
* **β (beta)** → brightness control (keep 0 for contrast only)

---

## ✅ Python Code: Contrast Variations

```python
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
```

---

## 📝 Comment on Results (Exam / Viva Ready)

* **Low contrast image**
  Pixel intensity differences are reduced, making the image appear **faded and flat**.

* **Original image**
  Shows the **natural contrast** captured by the camera.

* **High contrast image**
  Bright areas become brighter and dark areas darker, improving **edge visibility** but may cause **loss of details** in extreme regions.

---

## ✅ Final Conclusion (1–2 lines)

Contrast variation significantly affects image visibility and detail perception. Increasing contrast enhances edges and features, while decreasing contrast reduces visual clarity.

---

If you want next:

* **Histogram-based contrast analysis**
* **Histogram Equalization**
* **CLAHE (advanced contrast enhancement)**

tell me 👉
