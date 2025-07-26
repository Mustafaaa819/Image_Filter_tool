from PIL import Image
import numpy as np
from Filters.grayscale import grayScaling_image

def black_and_white(img_arr, threshold=128):
    gray = grayScaling_image(img_arr)

    bw = np.where(gray > threshold, 255, 0).astype(np.uint8)
    bw = np.stack([bw]*3, axis=-1)

    return Image.fromarray(bw)