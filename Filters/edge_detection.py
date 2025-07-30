from PIL import  Image
import numpy as np

image = Image.open('img.jpg').convert('L')
img_arr = np.array(image)

sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

sobel_y = np.array([
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
])

def edge_detection(img_arr, sobel_x, sobel_y):
    height, width = img_arr.shape
    edges = np.zeros_like(img_arr)
    padded_image = np.pad(img_arr, pad_width=1, mode='edge')

    for i in range(1, height+1):
        for j in range(1, width+1):
            matrix = padded_image[i-1:i+2, j-1:j+2]
            gx = np.sum(sobel_x * matrix)
            gy = np.sum(sobel_y * matrix)
            magnitude = np.sqrt(gx**2 + gy**2)
            edges[i-1,j-1] = np.clip(magnitude, 0, 255)

    return edges.astype(np.uint8)


