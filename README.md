# 🖼️ Image Filter Tool

A simple Python project to apply filters to images using PIL and NumPy.

---

## 🚀 Features
- Grayscale
- Sepia
- Invert Colors
- Darken
- Brightness Adjustment
- Contrast Control
- Black & White (Thresholding)

---

## Short Explanations of Filters:
- ## Grayscale: 
- I took the mean of the image array and RGB values of the image pixels, and all colors are gone just pale gray.

- ## Sepia:
- I took the sepia filter values and converted them into an array using numpy, then i took transpose of the sepia coordinates for correct alignment. Then   i used a dot product of sepia coordinates and the image array and clipped    the values between 0-255 and the picture was that of vintage, nostalgic look

- ## Invert Colors:
- It was quite simple to invert. I just subtracted the image's pixel values (RGB) from the highest pixel value 255 and picture's colors were upside down.

- ## Darken Image:
- I just divided the image pixel values by 2 to make the intensity of pixels half and picture's sun was setting down making it dark.

- ## Brightness Adjustment:
- I used a brightness factor (0, 1.5, 2), more the brightness factor, more     brighter the image. I multiplied the factor and the image array and if the some value exceeded beyond 255 it is clipped to 255 and image is brighter.

- ## Contrast Adjustment:
- I used once again another factor, contrast factor: more the contrast factor  
  dark will become darker and bright will become brighter. values will be stretched from the center. And lesser the factor, all colors will tend to move towards the center, pale gray. and all this will happen with this formula: (img_arr - 128) * contrast_factor + 128

- ## Black and White:
  This was one tough one to conquer. Remember the grayscale? we'll use that grayscale to turn the image into black and white. First we'll get that average number returned by the mean of RGB (for grayscale) and then will compare that average with threshold, if it's greater than threshold(i.e.128) then it is set to 255 otherwise it is set to zero(black).


---

## ⚙️ How to Run

1. Clone this repo:
```bash
git clone https://github.com//Image_Filter_tool.git
Navigate to the folder:
cd Image_Filter_tool

Install dependencies:
pip install -r requirements.txt

Run the app:
python main.py

📦 Requirements
Pillow
NumPy

dev: mustafaaa🤖
powered by pillow, numpy and python