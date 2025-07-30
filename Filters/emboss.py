import numpy as np

emboss_kernel = ([
    [-2, -1, 0],
    [-1, 1, 1],
    [0, 1, 2]
])

def emboss_filter(image,kernel):
    height = image.shape[0]
    width = image.shape[1]

    emboss_img = np.zeros_like(image)
    padding = np.pad(image, pad_width=1, mode='edge')

    for i in range(1, height+1):
        for j in range(1, width+1):
            matrix = padding[i-1:i+2, j-1:j+2]
            value = np.sum(kernel * matrix)
            emboss_img[i-1,j-1] = np.clip(value, 0, 255)
    return emboss_img.astype(np.uint8)
