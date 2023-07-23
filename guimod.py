import tkinter as tk
from tkinter import filedialog
import customtkinter
from PIL import ImageTk, Image
from coloring import colorip
import matlab.engine
import color_propagation
from color_propagation import rough
from color_propagation import colorizer
from color_propagation import colorizationSolver
from color_propagation import colorConversion
from artifact_removal import main
from metrics import metrics
class ImageUploader:
    def __init__(self, master):
        self.master = master
        self.master.title("Image Uploader")
        self.master.config(bg="#303030")
        self.master.option_add('*Font', 'TkDefaultFont 10')
        #self.upload_button = tk.Button(self.master, text="Upload", command=self.browse_files)
        #self.upload_button.pack(pady=10)
        #self.upload_button = tk.Button(self.master, text="Upload", command=self.browse_files, bg="#0077cc", fg="white", bd=0, padx=20, pady=10, activebackground="#0066aa", activeforeground="white")
        #self.upload_button.pack(pady=10)
        self.upload_button = customtkinter.CTkButton(self.master, text="Upload",command=self.browse_files,font=("Calibri", 20))
        #self.upload_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        self.upload_button.pack(pady=50)
        self.loading_label = tk.Label(self.master, text="Click upload to select an image",font=("Calibri", 14))
        self.loading_label.pack()

        self.image_frame1 = tk.Frame(self.master, bg="#303030",pady=100)
        self.image_frame1.pack(side=tk.LEFT, padx=10, pady=10, fill="both", expand=True, anchor="center")

        self.image_label1 = tk.Label(self.image_frame1)
        self.image_label1.pack(side=tk.TOP, fill="both", expand=True)

        self.image_label1_text = tk.Label(self.image_frame1, text="", font=("Arial", 12), fg="white", bg="#303030")
        self.image_label1_text.pack(side=tk.BOTTOM, pady=10)

        self.image_frame2 = tk.Frame(self.master, bg="#303030",pady=100)
        self.image_frame2.pack(side=tk.LEFT, padx=10, pady=10, fill="both", expand=True, anchor="center")

        self.image_label2 = tk.Label(self.image_frame2)
        self.image_label2.pack(side=tk.TOP, fill="both", expand=True)

        self.image_label2_text = tk.Label(self.image_frame2, text="", font=("Arial", 12), fg="white", bg="#303030")
        self.image_label2_text.pack(side=tk.BOTTOM, pady=10)

        self.image_frame3 = tk.Frame(self.master, bg="#303030",pady=100)
        self.image_frame3.pack(side=tk.LEFT, padx=10, pady=10, fill="both", expand=True, anchor="center")

        self.image_label3 = tk.Label(self.image_frame3)
        self.image_label3.pack(side=tk.TOP, fill="both", expand=True)

        self.image_label3_text = tk.Label(self.image_frame3, text="", font=("Arial", 12), fg="white", bg="#303030")
        self.image_label3_text.pack(side=tk.BOTTOM, pady=10)
        self.loading_label.config(bg="#303030", fg="white")

        self.image_label1.config(bg="#303030")
        self.image_label2.config(bg="#303030")
        self.image_label3.config(bg="#303030")

    def browse_files(self):
        filetypes = (("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*"))
        colorize = filedialog.askopenfilename(initialdir="/", title="Select a file", filetypes=filetypes)
        if colorize:
            colorize= colorize.replace("gray", "color")
            colorize =colorize.replace("png", "jpg")
            self.display_images(colorize)
            
    def display_images(self, filename):
        self.loading_label.config(text="Colorizing image...")
        self.master.update()
        eng = matlab.engine.start_matlab()
        s=eng.genpath('Daisy')
        eng.addpath(s,nargout=0)
        self.loading_label.config(text="extracting features...")
        self.master.update()
        eng.testing(filename,nargout=0)
        
        eng.quit()
        self.loading_label.config(text="colorizing interest points...")
        self.master.update()
        colorip(filename)
        rough.rough()
        colorizer.propagate()
        self.loading_label.config(text="propagating colors and removing artifacts...")
        self.master.update()
        main.test_color()  
        l=metrics(filename,'filter.png')  
        values = "PSNR: {:.2f}  dB\nSSIM: {:.2f}  %".format(l[0], l[1]*100)
        self.loading_label.config(text=values)
        self.master.update()
        image1 = Image.open('gray.png')
        image1 = image1.resize((320, 240), Image.ANTIALIAS)
        photo1 = ImageTk.PhotoImage(image1)
        self.image_label1.config(image=photo1)
        self.image_label1.image = photo1
        self.image_label1_text.config(text='grayscale image')
        image2 = Image.open('partial.png')
        image2 = image2.resize((320, 240), Image.ANTIALIAS)
        photo2 = ImageTk.PhotoImage(image2)
        self.image_label2.config(image=photo2)
        self.image_label2.image = photo2
        self.image_label2_text.config(text='partially colorized image')

        image3 = Image.open('filter.png')
        image3 = image3.resize((320, 240), Image.ANTIALIAS)
        photo3 = ImageTk.PhotoImage(image3)
        self.image_label3.config(image=photo3)
        self.image_label3.image = photo3
        self.image_label3_text.config(text='colorized image')
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry(f"{width}x{height}+0+0")

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("800x400")
    ImageUploader(root)
    root.mainloop()
