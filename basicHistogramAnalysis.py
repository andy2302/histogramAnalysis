import cv2
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class HistogramAnalysis(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Histogram Analysis")
        self.geometry('1000x1000')

        # Create a toolbar frame
        self.toolbar_frame = tk.Frame(self)
        self.toolbar_frame.pack(side=tk.TOP, fill=tk.X)

        # Button to open the file dialog
        self.open_file_button = tk.Button(self.toolbar_frame, text="Open Image", command=self.open_image)
        self.open_file_button.pack(side=tk.LEFT)

        # Button to exit the program
        self.exit_button = tk.Button(self.toolbar_frame, text="Exit", command=self.quit)
        self.exit_button.pack(side=tk.LEFT)

    def open_image(self):
        # Open a file dialog to select an image file
        self.filename = filedialog.askopenfilename()

        # Load the image
        img = cv2.imread(self.filename)

        # Clear any existing widgets in the main window
        for widget in self.winfo_children():
            if widget != self.toolbar_frame:
                widget.destroy()

        # Create an instance of ProcessImage and pass the image
        self.process_image_window = ProcessImage(self, img)


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

        # Create a figure and subplots
        fig, axs = plt.subplots(2, 2, figsize=(20, 20))

        # Plot the original image
        axs[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        axs[0, 0].set_title('Original Image')
        axs[0, 0].axis('off')

        # Plot the color histograms
        axs[0, 1].set_title('Color Histogram')
        axs[0, 1].set_xlabel('Pixel Value')
        axs[0, 1].set_ylabel('Frequency')
        axs[0, 1].grid('on')
        axs[0, 1].plot(r_hist, color='r')
        axs[0, 1].plot(g_hist, color='g')
        axs[0, 1].plot(b_hist, color='b')
        axs[0, 1].set_xlim([0, 256])

        # Plot the grayscale image
        axs[1, 0].imshow(gray, cmap='gray')
        axs[1, 0].set_title('Grayscale Image')
        axs[1, 0].axis('off')

        # Plot the grayscale histogram
        axs[1, 1].set_title('Grayscale Histogram')
        axs[1, 1].set_xlabel('Pixel Value')
        axs[1, 1].set_ylabel('Frequency')
        axs[1, 1].grid('on')
        axs[1, 1].plot(hist, color='gray')
        axs[1, 1].set_xlim([0, 256])

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
