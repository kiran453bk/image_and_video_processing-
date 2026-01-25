

### 1️⃣ Original Grayscale Image

* Full range of intensity (0–255) is preserved.
* Fine details, textures, and subtle variations are visible.
* This serves as the reference for comparison.

---

### 2️⃣ Reconstructed Image (All 8 Bit Planes)

* Looks **identical** to the original grayscale image.
* Reason: All bit planes (0–7) are used, so **no information is lost**.
* Confirms that bit-plane decomposition and reconstruction are correct.

---

### 3️⃣ Reconstructed Image (MSB Planes 5–7)

* Appears **coarser and posterized**.
* Fine details and small intensity variations are missing.
* Only major intensity differences (due to the most significant bits) are preserved.
* This demonstrates that **MSBs capture the overall shape and structure**, but not subtle textures.

---

### 4️⃣ Difference Map (Original − MSB Reconstructed)

* Highlights the information **lost by ignoring LSB planes (0–4)**.
* Bright regions in the difference map indicate areas with more lost detail.
* Dark regions indicate areas where MSB planes were sufficient to approximate intensity.
* Confirms that **lower bit planes contribute mostly to fine details and subtle variations**.

---

### 🔹 Key Takeaways

1. **All 8 bits** → perfect reconstruction, no loss.
2. **MSB 5–7 only** → preserves coarse image structure, loses fine details.
3. **LSB planes** (0–4) → mainly contribute to texture, subtle variations, and noise.
4. Bit-plane analysis is useful in **image compression, watermarking, and highlighting important intensity features**.

