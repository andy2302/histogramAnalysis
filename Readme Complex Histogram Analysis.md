# Histogram Analysis in Python and OpenCV

This Python program provides a graphical user interface (GUI) to analyze and display histograms of an image using OpenCV and Matplotlib. The application reads an input image, calculates histograms for the color channels (red, green, and blue) and grayscale, and displays these histograms in a set of subplots. Additionally, it calculates the cumulative distribution function (CDF) for the grayscale image and displays values for black, shadows, midtones, highlights, and whites.

## Dependencies
To run this program, you need to have the following Python libraries installed:

- NumPy
- OpenCV (cv2)
- Matplotlib
- Tkinter

## How to Use

1. Run the program by executing the Python script. A window titled "Histogram Analysis" will appear.
2. Click on "File" in the menu bar and select "Open Image" to open a file dialog for selecting an image file.
3. Once you have selected an image, the application will display the following:
- Original Image
- Red Channel Histogram
- Green Channel Histogram
- Blue Channel Histogram
- Grayscale Image
- Grayscale Histogram
- Combined Color Histogram (Red, Green, and Blue)
- Overlaid Histograms (Red, Green, Blue, and Gray)
4. The application will also display values for black, shadows, midtones, highlights, and whites based on the CDF of the grayscale image.
5. You can use the toolbar below the subplots to navigate and interact with the displayed histograms.

## Code Explanation

The code is organized into two main classes: _HistogramAnalysis_ and _ProcessImage_.

### HistogramAnalysis Class

**_HistogramAnalysis_** inherits from the _**tk.Tk**_ class and sets up the main window of the application. It creates a menu bar with a "File" menu, which includes the "Open Image" and "Exit" actions. The class also creates a content frame, where the histograms and image data will be displayed once an image is loaded.

#### `__init__` method
The constructor of the HistogramAnalysis class initializes the main window, sets the title and dimensions, and creates the menu bar and content frame.

```
def __init__(self):
    super().__init__()
        
    screen_width = self.winfo_screenwidth()
    screen_height = self.winfo_screenheight()
    
    self.title("Histogram Analysis")
    self.geometry(f"{screen_width}x{screen_height}")
```
    
Create a menu bar
```
    menubar = tk.Menu(self)
    self.config(menu=menubar)
``` 
Create a "File" menu
```
    file_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=file_menu)
``` 
Add "Open Image" action to the "File" menu
```
    file_menu.add_command(label="Open Image", command=self.open_image)
```
Add "Exit" action to the "File" menu
```
    file_menu.add_command(label="Exit", command=self.quit)
``` 
Create a frame for the canvas and toolbar
```
    self.content_frame = tk.Frame(self)
    self.content_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
```

#### `open_image` method
The `open_image` method opens a file dialog to select an image file, reads the image using OpenCV, and clears any existing widgets in the content frame. It then creates an instance of the `ProcessImage` class, passing the content frame and the loaded image.

```
    def open_image(self):
```
Open a file dialog to select an image file
```
        self.filename = filedialog.askopenfilename()
```
Load the image
```
        img = cv2.imread(self.filename)
```
Clear any existing widgets in the content frame
```
        for widget in self.content_frame.winfo_children():
            widget.destroy()
```
Create an instance of ProcessImage and pass the image
```
        self.process_image_window = ProcessImage(self.content_frame, img)
```

### ProcessImage Class
_**ProcessImage**_ is responsible for processing the input image, calculating the histograms, and displaying them in the content frame.

#### `__init__` method
The constructor of the **_ProcessImage_** class calculates the color histograms for the red, green, and blue channels, and the grayscale histogram for the grayscale version of the input image. It also calculates the cumulative distribution function for the grayscale image and the corresponding values for black, shadows, midtones, highlights, and whites. Finally, it creates labels for these values and displays them at the top of the content frame.

The constructor then creates a set of subplots using Matplotlib, displaying the original image, grayscale image, histograms for the red, green, and blue channels, combined color histogram, and overlaid histograms. It creates a canvas to display the subplots in the content frame and adds a toolbar for navigation and interaction.

#### Running the Application
At the end of the script, an instance of the HistogramAnalysis class is created and the Tkinter main loop is started, which runs the application.

When you run the program, the main window will open, allowing you to select an image and view the histograms and related information. You can interact with the displayed histograms using the toolbar provided below the subplots.

## License
This project is open source and available under the MIT License.