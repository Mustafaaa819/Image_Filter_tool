import numpy as np
from PIL import Image

sharpening_kernel = [
    [-1,-1,-1],
    [-1,9,-1],
    [-1,-1,-1]
]
sharpening_kernel = np.array(sharpening_kernel)

def sharpen_image(image,kernel):
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]

    k = kernel.shape[0]//2

    empty_arr = np.zeros_like(image)
    padded_image = np.pad(image, ((k,k),(k,k),(0,0)), mode='edge')

    for i in range(height):
        for j in range(width):
            for c in range(channels):
                grid = padded_image[i:i+3, j:j+3, c]
                convolution = np.sum(grid*kernel)
                empty_arr[i,j,c] = np.clip(convolution,0,255)
    return empty_arr






















