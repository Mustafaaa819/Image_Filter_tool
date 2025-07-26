from PIL import Image
import numpy as np

def grayScaling_image(img_arr):
    gray = np.mean(img_arr, axis=2).astype(np.uint8)
    return gray
    # gray_image = np.stack([gray, gray, gray], axis=-1)
    # return Image.fromarray(gray_image)
