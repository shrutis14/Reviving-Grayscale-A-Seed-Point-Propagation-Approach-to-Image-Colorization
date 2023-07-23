import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import matlab.engine
# Define a function that takes an image file path as an argument
def process_image(image_path):
    # Replace this with your actual image processing code
    print("Processing image:", image_path)

# Create the GUI application
root = tk.Tk()
root.withdraw()

# Ask the user to select an image file
file_path = filedialog.askopenfilename(
    title="Select an image file",
    filetypes=(("Image files", "*.jpg;*.png;*.bmp"), ("All files", "*.*"))
)

# Load the selected image using Pillow
image = Image.open(file_path)
import matlab.engine
eng = matlab.engine.start_matlab()
s=eng.genpath('Daisy')
eng.addpath(s,nargout=0)
eng.testing(file_path,nargout=0)
eng.quit()

# Display the selected image in the GUI
photo = ImageTk.PhotoImage(image)
label = tk.Label(root, image=photo)
label.pack()

# Pass the selected file path to the process_image function
#process_image(file_path)

# Start the GUI event loop
#root.mainloop()
