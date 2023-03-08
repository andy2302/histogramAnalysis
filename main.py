# 7. Analyze an Image Using Histogram in Python and OpenCV

import cv2
import numpy as np
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Create a Tkinter window
root = tk.Tk()
root.withdraw()

# Open a file dialog to select an image
file_path = filedialog.askopenfilename()

# Load the selected image
img = cv2.imread(file_path)

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate the histogram for grayscale image
hist_gray = cv2.calcHist([gray], [0], None, [256], [0, 256])

# Split the image into channels
b, g, r = cv2.split(img)

# Calculate the histogram for each channel
hist_b = cv2.calcHist([b], [0], None, [256], [0, 256])
hist_g = cv2.calcHist([g], [0], None, [256], [0, 256])
hist_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Calculate the cumulative distribution function for grayscale image
cdf_gray = hist_gray.cumsum()
cdf_gray_normalized = cdf_gray / cdf_gray.max()

# Calculate the cumulative distribution function for each channel
cdf_b = hist_b.cumsum()
cdf_b_normalized = cdf_b / cdf_b.max()
cdf_g = hist_g.cumsum()
cdf_g_normalized = cdf_g / cdf_g.max()
cdf_r = hist_r.cumsum()
cdf_r_normalized = cdf_r / cdf_r.max()

# Calculate the values for black, shadows, midtones, highlights, and whites
black = np.where(cdf_gray_normalized >= 0.01)[0][0]
shadows = np.where(cdf_gray_normalized >= 0.25)[0][0]
midtones = np.where(cdf_gray_normalized >= 0.5)[0][0]
highlights = np.where(cdf_gray_normalized >= 0.75)[0][0]
whites = np.where(cdf_gray_normalized >= 0.99)[0][0]

# Display the values for black, shadows, midtones, highlights, and whites
print("Black: {}".format(black))
print("Shadows: {}".format(shadows))
print("Midtones: {}".format(midtones))
print("Highlights: {}".format(highlights))
print("Whites: {}".format(whites))

# Plot the histograms for grayscale image and each channel
plt.subplot(2, 2, 1)
plt.plot(hist_gray)
plt.title("Grayscale Image")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")

plt.subplot(2, 2, 2)
plt.plot(hist_b, color='blue')
plt.title("Blue Channel")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")

plt.subplot(2, 2, 3)
plt.plot(hist_g, color='green')
plt.title("Green Channel")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")

plt.subplot(2, 2, 4)
plt.plot(hist_r, color='red')
plt.title("Red Channel")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")

plt.show()

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()
