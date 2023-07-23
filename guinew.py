import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from coloring import colorip
import matlab.engine
import color_propagation
from color_propagation import rough
from color_propagation import colorizer
from color_propagation import colorizationSolver
from color_propagation import colorConversion
from artifact_removal import main
class ImageUploader:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Uploader")

        self.upload_button = tk.Button(self.master, text="Upload", command=self.browse_files)
        self.upload_button.pack(pady=10)

        self.image_label = tk.Label(self.master)
        self.image_label.pack()

    def browse_files(self):
        filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
        filename = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=filetypes)
        if filename:
            self.display_image(filename)
            Str = filename[:len(filename)-4]
            #print(Str)
            #print(filename)

    def display_image(self, filename):
        image = Image.open(filename)
        image = image.resize((320, 240), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.image_label.config(image=photo)
        self.image_label.image = photo
        eng = matlab.engine.start_matlab()
        s=eng.genpath('Daisy')
        eng.addpath(s,nargout=0)
        eng.testing(filename,nargout=0)
        eng.quit()
        colorip()
        rough.rough()
        colorizer.propagate()
        main.test_color()

if __name__ == '__main__':
    root = tk.Tk()
    ImageUploader(root)
    root.mainloop()
