# import numpy as np
# from PIL import Image
#
# sharpening_kernel = [
#     [-1,-1,-1],
#     [-1,9,-1],
#     [-1,-1,-1]
# ]
# sharpening_kernel = np.array(sharpening_kernel)
#
# def sharpen_image(image,kernel):
#     height = image.shape[0]
#     width = image.shape[1]
#     channels = image.shape[2]
#
#     k = kernel.shape[0]//2
#
#     empty_arr = np.zeros_like(image)
#     padded_image = np.pad(image, ((k,k),(k,k),(0,0)), mode='edge')
#
#     for i in range(height):
#         for j in range(width):
#             for c in range(channels):
#                 grid = padded_image[i:i+3, j:j+3, c]
#                 convolution = np.sum(grid*kernel)
#                 empty_arr[i,j,c] = np.clip(convolution,0,255)
#     return empty_arr







from PIL import  Image
import numpy as np

sharpening_kernel = np.array ([
    [-1, -1, -1],
    [-1, 9, -1],
    [-1, -1, -1]
])

def sharpen_the_image(image, kernel):
    height = image.shape[0]
    width = image.shape[1]
    channels = image.shape[2]

    k = kernel.shape[0] // 2 #offset from the center

    sharpened_image = np.zeros_like(image)
    padding = np.pad(image, ((k, k), (k, k), (0, 0)), mode='edge')

    for i in range(k, height+k):
        for j in range(k, width+k):
            for c in range(channels):
                matrix = padding[i-1:i+2, j-1:j+2, c]
                value = np.sum(matrix * kernel)
                sharpened_image[i-k, j-k, c] = np.clip(value, 0, 255)
    return sharpened_image.astype(np.uint8)





















