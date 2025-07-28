from PIL import Image
import numpy as np

from Filters.grayscale import grayScaling_image
from Filters.brightness import apply_brightness
from Filters.contrast import apply_contrast
from Filters.sepia import apply_sepia
from Filters.darken import darken_image
from Filters.invert import invert_image
from Filters.black_white import black_and_white
from Filters.blur import blur_image

#Load the Image:
image = Image.open('img.jpg')

#Convert the Image(pixels) into a numpy array:
img_arr = np.array(image)

#Apply Filters:
gray_arr = grayScaling_image(img_arr)
sepia_img = apply_sepia(img_arr)
inverted_img = invert_image(img_arr)
bright_img = apply_brightness(img_arr,1)
dark_img = darken_image(img_arr)
contrast_img = apply_contrast(img_arr, 1.1)
bw_img = black_and_white(img_arr, 128)
blur_the_image = blur_image(img_arr)

#Save the Outputs:
Image.fromarray(gray_arr).save('gray.jpg')
sepia_img.save('sepia.jpg')
inverted_img.save('inverted.jpg')
bright_img.save('bright.jpg')
dark_img.save('dark.jpg')
contrast_img.save('contrast.jpg')
bw_img.save('bw.jpg')
blur_the_image.save('blur.jpg')