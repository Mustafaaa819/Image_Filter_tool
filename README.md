# 🧠 Edge Detection Filter (Sobel) – Image Filter Tool

The Edge Detection filter works by using **Sobel operator** to find edges of the image. It works when there is a sudden change in the intensity of the pixels, and it says "a sudden change, it is an edge."

---

## ⚙️ How It Works

I applied two 3×3 convolution kernels:

- `sobel_x` detects **horizontal edges**  
- `sobel_y` detects **vertical edges**

I computed the gradient magnitude at each pixel to identify edges:
  
\[
\text{magnitude} = \sqrt{(G_x)^2 + (G_y)^2}
\]

---

## 🛠 How to Run

1. Add your grayscale image (or convert it in `main.py`)
2. Define the `sobel_x` and `sobel_y` kernels
3. Call `edge_detection(image_array, sobel_x, sobel_y)`
4. Save the returned image

Example usage in `main.py`:

```python
from PIL import Image
import numpy as np
from Filters.edge_detection import edge_detection

# Load and convert image to grayscale
image = Image.open("img.jpg").convert('L')
img_arr = np.array(image)

# Define Sobel kernels
sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])
sobel_y = np.array([
    [-1, -2, -1],
    [ 0,  0,  0],
    [ 1,  2,  1]
])

# Apply edge detection
edges = edge_detection(img_arr, sobel_x, sobel_y)
Image.fromarray(edges).save("edges.jpg")
