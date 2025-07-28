# Blur Filter Module

This branch contains the implementation of a basic **Box Blur** filter using NumPy and Pillow.

## How It Works

- Loads an image using PIL
- Converts it into a NumPy array
- Applies a Box Blur using a 3x3 kernel around each pixel
- Saves the blurred output as `blur.jpg`

## Usage

```bash
python blur.py
