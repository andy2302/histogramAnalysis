import cv2
import matplotlib.pyplot as plt
from tkinter import filedialog, Tk

# Create a Tkinter root window, which will be hidden
root = Tk()
root.withdraw()

# Use a file dialog to select an image file
file_path = filedialog.askopenfilename()

# Load the image
img = cv2.imread(file_path)

# Calculate the histograms for each color channel
b_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
g_hist = cv2.calcHist([img], [1], None, [256], [0, 256])
r_hist = cv2.calcHist([img], [2], None, [256], [0, 256])

# Display the image and histograms
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
axs[0, 0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')
axs[0, 1].plot(b_hist, color='b')
axs[0, 1].set_xlim([0, 256])
axs[0, 1].set_title('Blue Histogram')
axs[1, 0].plot(g_hist, color='g')
axs[1, 0].set_xlim([0, 256])
axs[1, 0].set_title('Green Histogram')
axs[1, 0].set_xlabel('Pixel Value')
axs[1, 0].set_ylabel('Frequency')
axs[1, 1].plot(r_hist, color='r')
axs[1, 1].set_xlim([0, 256])
axs[1, 1].set_title('Red Histogram')
axs[1, 1].set_xlabel('Pixel Value')

# Adjust the layout and show the plot
plt.tight_layout()
plt.show()
