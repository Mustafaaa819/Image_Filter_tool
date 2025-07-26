from PIL import Image
import numpy as np

def grayScaling_image(img_arr):
    gray = np.mean(img_arr, axis=2).astype(np.uint8)
    return gray
    # gray_image = np.stack([gray, gray, gray], axis=-1)
    # return Image.fromarray(gray_image)
    # This returns a number that is the average of 3 colors, red, green and blue because to make a picture black and white we first need it's pixels to be around the center that is 128 (0-2550. We then use this function in the black_white.py to get that average number and then this average no is compared with the threshold number.
    #and then we use this function again in the main to get an average number and by saving it, it becomes the gray picture. It's just the game of NUMBERS.
