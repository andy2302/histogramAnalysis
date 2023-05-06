# 7. Analyze an Image Using Histogram in Python and OpenCV

import numpy as np
import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class HistogramAnalysis(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Histogram Analysis")
        self.geometry('1200x800')

        # Create a menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Create a "File" menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)

        # Add "Open Image" action to the "File" menu
        file_menu.add_command(label="Open Image", command=self.open_image)

        # Add "Exit" action to the "File" menu
        file_menu.add_command(label="Exit", command=self.quit)

        # Create a frame for the canvas and toolbar
        self.content_frame = tk.Frame(self)
        self.content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def open_image(self):
        # Open a file dialog to select an image file
        self.filename = filedialog.askopenfilename()

        # Load the image
        img = cv2.imread(self.filename)

        # Clear any existing widgets in the content frame
        for widget in self.content_frame.winfo_children():
            widget.destroy()

        # Create an instance of ProcessImage and pass the image
        self.process_image_window = ProcessImage(self.content_frame, img)


class ProcessImage:
    def __init__(self, parent, img):
        self.parent = parent

        # Calculate the color histograms
        b_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
        g_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
        r_hist = cv2.calcHist([img], [2], None, [256], [0, 256])

        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Calculate the grayscale histogram
        hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

        # Calculate the cumulative distribution function for grayscale image
        cdf_gray = hist.cumsum()
        cdf_gray_normalized = cdf_gray / cdf_gray.max()

        # Calculate the values for black, shadows, midtones, highlights, and whites
        black = np.where(cdf_gray_normalized >= 0.01)[0][0]
        shadows = np.where(cdf_gray_normalized >= 0.25)[0][0]
        midtones = np.where(cdf_gray_normalized >= 0.5)[0][0]
        highlights = np.where(cdf_gray_normalized >= 0.75)[0][0]
        whites = np.where(cdf_gray_normalized >= 0.99)[0][0]

        # Create labels for black, shadows, midtones, highlights, and whites
        label_frame = tk.Frame(self.parent)
        label_frame.pack(side=tk.TOP, pady=10)

        tk.Label(label_frame, text=f"Black: {black}").grid(row=0, column=0, padx=5)
        tk.Label(label_frame, text=f"Shadows: {shadows}").grid(row=0, column=1, padx=5)
        tk.Label(label_frame, text=f"Midtones: {midtones}").grid(row=0, column=2, padx=5)
        tk.Label(label_frame, text=f"Highlights: {highlights}").grid(row=0, column=3, padx=5)
        tk.Label(label_frame, text=f"Whites: {whites}").grid(row=0, column=4, padx=5)

        # Create a figure and subplots
        fig, axs = plt.subplots(2, 4, figsize=(20, 10))

        # Plot the original image
        axs[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        axs[0, 0].set_title('Original Image')
        axs[0, 0].axis('off')

        # Plot the red channel histogram
        axs[0, 1].plot(r_hist, color='r')
        axs[0, 1].set_title('Red Channel')
        axs[0, 1].set_xlabel("Pixel Intensity")
        axs[0, 1].set_ylabel("Number of Pixels")

        # Plot the green channel histogram
        axs[0, 2].plot(g_hist, color='g')
        axs[0, 2].set_title('Green Channel')
        axs[0, 2].set_xlabel("Pixel Intensity")
        axs[0, 2].set_ylabel("Number of Pixels")

        # Plot the blue channel histogram
        axs[0, 3].plot(b_hist, color='b')
        axs[0, 3].set_title('Blue Channel')
        axs[0, 3].set_xlabel("Pixel Intensity")
        axs[0, 3].set_ylabel("Number of Pixels")

        # Plot the grayscale image
        axs[1, 0].imshow(gray, cmap='gray')
        axs[1, 0].set_title('Grayscale Image')
        axs[1, 0].axis('off')

        # Plot the grayscale histogram
        axs[1, 1].plot(hist, color='gray')
        axs[1, 1].set_title("Grayscale Histogram")
        axs[1, 1].set_xlabel("Pixel Intensity")
        axs[1, 1].set_ylabel("Number of Pixels")

        # Remove extra subplots
        axs[1, 2].axis('off')
        axs[1, 3].axis('off')

        # Adjust the layout and show the plot
        plt.tight_layout()

        # Create a canvas and display the plot on it
        canvas = FigureCanvasTkAgg(fig, master=self.parent)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Create a toolbar and display it
        toolbar = NavigationToolbar2Tk(canvas, self.parent)
        toolbar.update()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


# Create an instance of the HistogramAnalysis class and run the Tkinter main loop
app = HistogramAnalysis()
app.mainloop()
