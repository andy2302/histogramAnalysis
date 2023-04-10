# ImageEffects

This script provides a simple image processing application with a graphical user interface (GUI) using PyQt5. The application allows users to open an image, apply various image processing methods, and view the results.

### Dependencies

The script requires the following packages:

* opencv-python
* PyQt5
* matplotlib

Install these packages using pip:

`pip install opencv-python PyQt5 matplotlib`

### Usage

Run the script using Python 3:

`python ImageEffects.py`

This will launch the Image Processing application. The main window consists of a menu, buttons for applying image processing methods, and a slider for controlling the intensity of the effect.

### Features

The application supports the following image processing methods:

1. Brightening: Increases the brightness of the image by adding a constant value to the Y channel of the YCrCb color space.
2. Darkening: Decreases the brightness of the image by subtracting a constant value from the Y channel of the YCrCb color space.
3. Contrast Enhancement: Enhances the contrast of the image by multiplying the Y channel of the YCrCb color space by a constant value.
4. Contrast Decreasing: Decreases the contrast of the image by dividing the Y channel of the YCrCb color space by a constant value.
5. Thresholding or Image Binarization: Binarizes the image by setting pixel values above a threshold to the maximum value and pixel values below the threshold to the minimum value.

### Application Workflow

1. Open the Image Processing application by running the script.
2. Click on "File" in the menu bar and select "Open image" to open an image file.
3. Use the slider to adjust the intensity of the effect for the selected processing method.
4. Click on the desired processing method button to apply the method to the image.
5. The original and processed images will be displayed side by side in a separate window.

### Customization

You can modify the script to add new image processing methods, change the appearance of the GUI, or adjust the intensity range of the slider. To add a new method, follow these steps:

1. Add a new button for the method in the process_buttons dictionary in the initUI method.
2. Connect the button to the process_image method.
3. Add a new case for the method in the process_image_method function and implement the image processing operation.

To change the appearance of the GUI or adjust the intensity range, modify the appropriate properties and parameters in the initUI method.