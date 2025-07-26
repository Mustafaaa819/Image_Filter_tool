import numpy as np
from PIL import Image

def darken_image(img_arr):
    dark = img_arr//2
    return Image.fromarray(dark)