import cv2
import numpy as np
import matplotlib.pyplot as plt

# ---------- Read Image ----------
img = cv2.imread('demo.jpg', 0)   # grayscale
M, N = img.shape

# ---------- FFT ----------
F = np.fft.fft2(img)
F_shift = np.fft.fftshift(F)

# ---------- Spectrum ----------
magnitude_spectrum = np.log(1 + np.abs(F_shift))

# ---------- Distance Matrix ----------
u = np.arange(M)
v = np.arange(N)
U, V = np.meshgrid(u, v, indexing='ij')
D = np.sqrt((U - M/2)**2 + (V - N/2)**2)

D0 = 50     # cutoff frequency
n = 2       # Butterworth order

# ---------- Filters ----------

# Ideal LPF
H_ilpf = np.zeros((M,N))
H_ilpf[D <= D0] = 1

# Ideal HPF
H_ihpf = 1 - H_ilpf

# Butterworth LPF
H_blpf = 1 / (1 + (D/D0)**(2*n))

# Butterworth HPF
H_bhpf = 1 - H_blpf

# Gaussian LPF
H_glpf = np.exp(-(D**2)/(2*(D0**2)))

# Gaussian HPF
H_ghpf = 1 - H_glpf

# ---------- Apply Filters ----------
def apply_filter(H, Fshift):
    G = H * Fshift
    G_ishift = np.fft.ifftshift(G)
    img_back = np.fft.ifft2(G_ishift)
    return np.abs(img_back)

img_ilpf = apply_filter(H_ilpf, F_shift)
img_ihpf = apply_filter(H_ihpf, F_shift)
img_blpf = apply_filter(H_blpf, F_shift)
img_bhpf = apply_filter(H_bhpf, F_shift)
img_glpf = apply_filter(H_glpf, F_shift)
img_ghpf = apply_filter(H_ghpf, F_shift)

# ---------- Display ----------
plt.figure(); plt.title("Original Image"); plt.imshow(img, cmap='gray'); plt.axis('off')
plt.figure(); plt.title("FFT Spectrum"); plt.imshow(magnitude_spectrum, cmap='gray'); plt.axis('off')

plt.figure(); plt.title("Ideal LPF"); plt.imshow(img_ilpf, cmap='gray'); plt.axis('off')
plt.figure(); plt.title("Ideal HPF"); plt.imshow(img_ihpf, cmap='gray'); plt.axis('off')

plt.figure(); plt.title("Butterworth LPF"); plt.imshow(img_blpf, cmap='gray'); plt.axis('off')
plt.figure(); plt.title("Butterworth HPF"); plt.imshow(img_bhpf, cmap='gray'); plt.axis('off')

plt.figure(); plt.title("Gaussian LPF"); plt.imshow(img_glpf, cmap='gray'); plt.axis('off')
plt.figure(); plt.title("Gaussian HPF"); plt.imshow(img_ghpf, cmap='gray'); plt.axis('off')

plt.show()
