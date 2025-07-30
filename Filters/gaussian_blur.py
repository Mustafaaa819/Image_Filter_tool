from PIL import Image
import numpy as np

def build_gaussian_kernel(size=3, sigma=1):
    kernel = np.zeros((size, size), dtype=np.float32) #a grid initialized filled with zeros.
    k = size // 2 #this tell us the offset from the center, for example if this is a 3x3 grid, then 3//2 gives us 1 and this 1 here means, the center is 1 row and 1 column from the top left corner(starting).

    for i in range(size):
        for j in range(size):
                x = i - k
                y = j - k

                kernel[i,j] = (1 / (2 * np.pi * sigma ** 2)) * np.exp(-(x**2 + y**2))/(2*sigma**2) #Gaussian 2D Formula.
    kernel /= np.sum(kernel)
    return kernel


def apply_Gaussian_blur(image,kernel):
    k = kernel.shape[0]//2

    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]

    gaussian_blur_arr = np.zeros_like(image)

    for i in range(k, height-k):
        for j in range(k, width-k):
            for c in range(channels):
                patch = image[i-k:i+k+1, j-k:j+k+1, c]
                value = np.sum(patch*kernel)
                gaussian_blur_arr[i,j,c] = value

    return gaussian_blur_arr
















