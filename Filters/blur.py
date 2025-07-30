import numpy as np
from PIL import Image


def blur_image(img_arr):
    height = img_arr.shape[0]
    width = img_arr.shape[1]
    channels = img_arr.shape[2]

    #initialized an empty grid with all zero's in it.
    blurred = np.zeros_like(img_arr)

    for y in range(1,height-1):
        for x in range(1,width-1):
            for c in range(channels):
                #we make a 3x3 grid around pixel(y,x):
                block = img_arr[y-1:y+2, x-1:x+2, c]

                #then we take mean or average of all the numbers in grid:
                averaged = np.mean(block)

                #then we put this average value into the new image:
                blurred[y,x,c] = averaged

    return blurred


















