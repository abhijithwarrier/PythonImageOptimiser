# Programmer - python_scripts (Abhijith Warrier)

# PYTHON GUI APPLICATION TO OPTIMISE IMAGES

# PIL is the Python Imaging Library which provides the python interpreter with image editing capabilities.
# The Image module provides a class with the same name which is used to represent a PIL image.
# The module also provides a number of factory functions, including functions to load images from files,
# and to create new images.

# Importing necessary packages
import os
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

# Defining CreateWidgets() function to create necessary tkinter widgets
def CreateWidgets():
    root.inputImgLabel = Label(root, bg="darkseagreen4", fg="white", text="ORIGINAL IMAGE", font=('Comic Sans MS',20))
    root.inputImgLabel.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

    root.inputImage = Label(root, bg="darkseagreen4", borderwidth=3, relief="groove")
    root.inputImage.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

    root.imagePath = Entry(root, width=55, textvariable=imagePath)
    root.imagePath.grid(row=3, column=1, padx=10, pady=10)

    root.browseButton = Button(root, width=10, text="BROWSE", command=imageBrowse)
    root.browseButton.grid(row=3, column=2, padx=10, pady=10)

    root.compressBTN = Button(root, text="COMPRESS", command=Compress, bg="LIGHTBLUE", font=('Comic Sans MS',15), width=20)
    root.compressBTN.grid(row=4, column=1, padx=10, pady=10)

    root.previewlabel = Label(root, bg="darkseagreen4", fg="white", text="COMPRESSED IMAGE", font=('Comic Sans MS',20))
    root.previewlabel.grid(row=1, column=4, padx=10, pady=10, columnspan=2)

    root.imageLabel = Label(root, bg="darkseagreen4", borderwidth=3, relief="groove")
    root.imageLabel.grid(row=2, column=4, padx=10, pady=10, columnspan=2)

    imageView = Image.open("<YOUR_DEFAULT_PATH>")
    imageResize = imageView.resize((640, 480), Image.ANTIALIAS)
    imageDisplay = ImageTk.PhotoImage(imageResize)

    root.imageLabel.config(image=imageDisplay)
    root.imageLabel.photo = imageDisplay
    root.inputImage.config(image=imageDisplay)
    root.inputImage.photo = imageDisplay

# Defining imageBrowse() to browse for the images to be optimised
def imageBrowse():
    # Presenting user with a pop-up for directory selection. initialdir argument is optional
    # Retrieving the user-input destination directory and storing it in destinationDirectory
    # Setting the initialdir argument is optional. SET IT TO YOUR DIRECTORY PATH
    openDirectory = filedialog.askopenfilename(initialdir="YOUR DIRECTORY PATH")
    # Displaying the directory in the directory textbox
    imagePath.set(openDirectory)
    # Opening saved image using the open() of Image class which takes saved image as argument
    imageView = Image.open(openDirectory)
    # Resizing the image using Image.resize()
    imageResize = imageView.resize((640, 480), Image.LANCZOS)
    # Creating object of PhotoImage() class to display the frame
    imageDisplay = ImageTk.PhotoImage(imageResize)
    # Configuring the label to display the frame
    root.inputImage.config(image=imageDisplay)
    # Keeping a reference
    root.inputImage.photo = imageDisplay

# Defining Compress() to compress and save the image and display the image in the imageLabel
def Compress():
    # Fetching and storing the name of the input pdf along with the path
    input_file_path_name = imagePath.get()
    # Storing the destination path and name for images
    image_destination_path = os.path.dirname(os.path.abspath(input_file_path_name))
    image_name = os.path.basename(input_file_path_name.split(".")[0]) + \
                 "-compressed." + os.path.basename(input_file_path_name.split(".")[1])
    # Opening the original image
    img = Image.open(input_file_path_name)
    # Fetching the dimensions of the image
    height, width = img.size
    # Optimizing and saving the image
    compressed = img.resize((height, width), Image.LANCZOS)
    compressed.save(image_destination_path + "/" + image_name, optimize=True, quality=9)
    # Opening the saved image using the open() of Image class which takes the saved image as the argument
    saved_image = Image.open(image_destination_path + "/" + image_name)
    # Resizing the image using Image.resize()
    imageResize = saved_image.resize((640, 480), Image.LANCZOS)
    # Creating object of PhotoImage() class to display the frame
    imageDisplay = ImageTk.PhotoImage(imageResize)
    # Configuring the label to display the frame
    root.imageLabel.config(image=imageDisplay)
    # Keeping a reference
    root.imageLabel.photo = imageDisplay

# Creating object of tk class
root = tk.Tk()
# Setting the title, window size, background color and disabling the resizing property
root.title("PythonImageOptimiser")
root.geometry("1340x670")
root.resizable(False, False)
root.configure(background = "darkseagreen4")
# Creating tkinter variables
destPath = StringVar()
imagePath = StringVar()
# Calling the CreateWidgets() function
CreateWidgets()
# Defining infinite loop to run application
root.mainloop()
