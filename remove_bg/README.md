# Background Removal Script

This Python script allows you to automatically remove the background from an image. It uses the `rembg` library, a machine-learning model designed for background removal, and the `Pillow` library for image processing.

## Features

- **Automatic Background Removal**: Easily remove backgrounds from images using the power of machine learning.
- **Supports Multiple Formats**: Works with PNG, JPEG, and other common image formats.
- **Fast and Efficient**: Leverages optimized models for quick and accurate background removal.
- **Customizable Output**: Save output images with transparent backgrounds for further use in various projects.

## Prerequisites

Before using this script, ensure you have Python installed on your system (Python 3.6 or later is recommended).

You also need to install the following Python packages:
- `rembg`: The library used to remove the background from images.
- `Pillow`: A library for handling and saving images.

To install the required libraries, run:

```
pip install rembg Pillow
```

## Usage:

**Run the Script**

Use the script by specifying the input image path and output path. Here's an example command:

```
python remove_bg.p
```

**Modify the Input and Output Paths**

You can customize the paths for the input image and output image within the remove_bg.py script. Update the following lines:

```
input_image_path = 'input_image.png'  # Path to your input image
output_image_path = 'output_image.png'  # Path to save the output image without background
```
