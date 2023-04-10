# Brightening
# Darkening
# Contrast enhancement
# Contrast decreasing
# Thresholding or image binarization

import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, \
    QMainWindow, QMenu, QMenuBar, QAction, QFileDialog, QLabel, QPushButton, QSlider, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt


class ImageProcessingGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('File')

        openFile = QAction('Open image', self)
        openFile.triggered.connect(self.showDialog)
        fileMenu.addAction(openFile)

        self.process_buttons = {
            'brightening': QPushButton('Brightening', self),
            'darkening': QPushButton('Darkening', self),
            'contrast_enhancement': QPushButton('Contrast Enhancement', self),
            'contrast_decreasing': QPushButton('Contrast Decreasing', self),
            'thresholding': QPushButton('Thresholding', self),
        }

        for method, button in self.process_buttons.items():
            button.clicked.connect(lambda checked, m=method: self.process_image(m))

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setMaximum(300)  # for a less dramatic effect I would advise that the maximum should be 100

        vbox = QVBoxLayout()
        vbox.addWidget(self.slider)

        for button in self.process_buttons.values():
            vbox.addWidget(button)

        container = QWidget()
        container.setLayout(vbox)
        self.setCentralWidget(container)

        self.setWindowTitle('Image Processing')
        self.resize(1900, 1000)
        self.show()

        self.img_path = None
        self.img = None

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open image',
                                            filter='Images (*.png *.xpm *.jpg *.bmp *.tiff);;All Files (*)')

        if fname[0]:
            self.img_path = fname[0]
            self.img = cv2.imread(self.img_path)

    def process_image(self, method):
        if self.img is None:
            return

        value = self.slider.value()
        processed_img = self.process_image_method(self.img, method, value)
        self.display_images(self.img, processed_img)

    @staticmethod
    def process_image_method(img, method, value):
        ycrcb_img = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
        y, cr, cb = cv2.split(ycrcb_img)

        # algorithm can be improved especially the contrasts
        if method == 'brightening':
            y = cv2.add(y, value)
        elif method == 'darkening':
            y = cv2.subtract(y, value)
        elif method == 'contrast_enhancement':
            y = cv2.multiply(y, value)
        elif method == 'contrast_decreasing':
            y = cv2.divide(y, value)
        elif method == 'thresholding':
            _, y = cv2.threshold(y, value, 255, cv2.THRESH_BINARY)

        processed_ycrcb = cv2.merge((y, cr, cb))
        processed_img = cv2.cvtColor(processed_ycrcb, cv2.COLOR_YCrCb2BGR)

        return processed_img

    @staticmethod
    def display_images(original, processed):
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
        plt.title('Original Image')
        plt.axis('off')
        plt.subplot(1, 2, 2)
        plt.imshow(cv2.cvtColor(processed, cv2.COLOR_BGR2RGB))
        plt.title('Processed Image')
        plt.axis('off')
        plt.show()


def main():
    app = QApplication(sys.argv)
    ex = ImageProcessingGUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

# Improve the algorithms see the comments on top

# 1. Additional image processing methods: You can expand the script by adding more image processing methods,
# such as image resizing, rotation, flipping, filtering, or edge detection. To implement these features,
# you can use the OpenCV library and connect the new methods to the GUI.
#
# 2. Undo/Redo functionality: Implement an undo/redo feature to allow users to revert the image to a previous state or
# reapply the processing method after undoing. You can use a list or stack to store the history of processed images
# and actions.
#
# 3. Save processed images: Add a 'Save' option in the 'File' menu to save the processed images in various formats,
# such as JPEG, PNG, or TIFF. Use the cv2.imwrite() function from OpenCV to save the processed images.
#
# 4. Image preview: Show a real-time preview of the processed image as the user adjusts the slider or selects different
# processing methods. Update the processed image display based on the user's selection without needing to click
# the method button.
#
# 5. Zoom and pan: Implement zoom and pan functionality for the image display, enabling users to zoom in/out and pan
# the image for better inspection of the processed image.
#
# 6. Keyboard shortcuts: Add keyboard shortcuts for opening, saving, and applying processing methods, enhancing the
# usability of the application.
#
# 7. Batch processing: Allow users to select multiple images and apply the processing methods to all selected images
# simultaneously.
