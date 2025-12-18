import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:/Users/Basavaraj Kulkarani/OneDrive/Desktop/images/download.jpg")

if img is None:
    print("Image not found. Check the path.")
else:
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.axis("off")
    plt.title("Loaded Image")
    plt.show()
