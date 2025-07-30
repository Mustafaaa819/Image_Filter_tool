from PIL import Image
import numpy as np

from Filters import sharpen
from Filters.grayscale import grayScaling_image
from Filters.brightness import apply_brightness
from Filters.contrast import apply_contrast
from Filters.sepia import apply_sepia
from Filters.darken import darken_image
from Filters.invert import invert_image
from Filters.black_white import black_and_white
from Filters.blur import blur_image
from Filters.gaussian_blur import build_gaussian_kernel
from Filters.gaussian_blur import apply_Gaussian_blur
from Filters.sharpen import sharpen_image
from Filters.sharpen import sharpening_kernel
from Filters.edge_detection import edge_detection
from Filters.edge_detection import sobel_x,sobel_y
from Filters.emboss import emboss_filter, emboss_kernel

#Load the Image:
image = Image.open('img.jpg')

#Convert the Image(pixels) into a numpy array:
img_arr = np.array(image)

#Apply Filters:
# gray_arr = grayScaling_image(img_arr)
# sepia_img = apply_sepia(img_arr)
# inverted_img = invert_image(img_arr)
# bright_img = apply_brightness(img_arr,1)
# dark_img = darken_image(img_arr)
# contrast_img = apply_contrast(img_arr, 1.1)
# bw_img = black_and_white(img_arr, 128)
#Advance Filters:
#Box Blurr:
blur_the_image = blur_image(img_arr)
#Sharpening:
sharpen_the_image = sharpen_image(img_arr, sharpening_kernel)
#Edge Detection:
image = Image.open('img.jpg').convert('L')
img_arr = np.array(image)
detect_edges = edge_detection(img_arr, sobel_x, sobel_y)
#Emboss:
emboss_the_image = emboss_filter(img_arr, emboss_kernel)

#Gaussian Blur:
# kernel = build_gaussian_kernel(3,1)
# image_blur = apply_Gaussian_blur(img_arr, kernel)


#Save the Outputs:
# Image.fromarray(gray_arr).save('gray.jpg')
# sepia_img.save('sepia.jpg')
# inverted_img.save('inverted.jpg')
# bright_img.save('bright.jpg')
# dark_img.save('dark.jpg')
# contrast_img.save('contrast.jpg')
# bw_img.save('bw.jpg')
# Image.fromarray(blur_the_image).save('box_blur.jpg')
# Image.fromarray(image_blur).save('gaussian_blur.jpg')
# Image.fromarray(sharpen_the_image).save('sharpen.jpg')
# Image.fromarray(detect_edges).save('edges_detection.jpg')
Image.fromarray(emboss_the_image).save('emboss_filter.jpg')