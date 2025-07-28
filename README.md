# Blur Filter Module

This branch contains the implementation of a basic **Box Blur** filter using NumPy and Pillow.

## Short Explanation of Logic:
- so basically what I did was just to make a 3x3 grid around a pixel, then took the mean of that grid and put the average value in the place of that specific pixel. The default structure for grid in python is (height,width,channels).
- Height is simply the number of rows stacked upon each other, and width is the no of columns.

## How It Works

- Loads an image using PIL
- Converts it into a NumPy array
- Applies a Box Blur using a 3x3 kernel around each pixel
- Saves the blurred output as `blur.jpg`

## Usage

```bash
python blur.py
