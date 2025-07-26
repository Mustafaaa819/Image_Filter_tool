import numpy as np
from PIL import Image

def apply_contrast(img_arr, contrast_factor):
    contrast_img = (img_arr - 128) * contrast_factor + 128
    contrast_img = np.clip(contrast_img, 0, 255).astype(np.uint8)
    return Image.fromarray(contrast_img)