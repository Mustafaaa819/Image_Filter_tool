from PIL import Image
import numpy as np

def invert_image(img_arr):
    inverted = 255 - img_arr
    return Image.fromarray(inverted)