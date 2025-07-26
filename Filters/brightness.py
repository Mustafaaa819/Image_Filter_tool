from PIL import Image
import numpy as np

def apply_brightness(img_arr, brightness_factor):
    brightness = img_arr * brightness_factor
    brightness = np.clip(brightness, 0, 255).astype(np.uint8)
    return Image.fromarray(brightness)