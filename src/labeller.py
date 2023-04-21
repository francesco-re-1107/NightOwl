import os
import shutil
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class Labeller:
    def __init__(self, master):
        self.master = master
        self.master.title("Labeller")
        self.master.resizable(False, False)
        
        
        self.current_image = None
        self.image_index = 0
        self.images = []
        self.folder_path = ""
        
        self.create_widgets()
        
        self.master.bind("<KeyPress>", self.on_key_press)
        
    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=888, height=500)
        self.canvas.grid(row=0, column=0, columnspan=4)
        
        self.btn_load = tk.Button(self.master, text="Load Images", command=self.load_images)
        self.btn_load.grid(row=1, column=0)
        
        self.btn_label_1 = tk.Button(self.master, text="Label 1", command=self.label_1)
        self.btn_label_1.grid(row=1, column=1)
        
        self.btn_label_2 = tk.Button(self.master, text="Label 2", command=self.label_2)
        self.btn_label_2.grid(row=1, column=2)
        
        self.btn_label_3 = tk.Button(self.master, text="Label 3", command=self.label_3)
        self.btn_label_3.grid(row=1, column=3)
        
    def load_images(self):
        self.folder_path = filedialog.askdirectory()
        if self.folder_path:
            files = [f for f in os.listdir(self.folder_path) if ".jpg" in f or ".png" in f]
            files = sorted(files, key=lambda x: int(x.split(".")[0]))
            
            for filename in files:
                if filename.endswith(".jpg") or filename.endswith(".png"):
                    image_path = os.path.join(self.folder_path, filename)
                    self.images.append(image_path)
            if self.images:
                self.show_image()
        
    def show_image(self):
        self.current_image = Image.open(self.images[self.image_index])
        self.current_image = self.current_image.resize((888, 500), Image.ANTIALIAS)
        self.current_image_filename = self.images[self.image_index]
        self.photo = ImageTk.PhotoImage(self.current_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        
    def label_1(self):
        if self.current_image:
            print("moving", self.current_image_filename, "to", os.path.join(self.folder_path, "1", os.path.basename(self.current_image_filename)))
            os.rename(self.current_image_filename, os.path.join(self.folder_path, "1", os.path.basename(self.current_image_filename)))
            self.images.pop(self.image_index)
            if self.images:
                self.image_index %= len(self.images)
                self.show_image()
            else:
                self.canvas.delete("all")
                
    def label_2(self):
        if self.current_image:
            print("moving", self.current_image_filename, "to", os.path.join(self.folder_path, "2", os.path.basename(self.current_image_filename)))
            os.rename(self.current_image_filename, os.path.join(self.folder_path, "2", os.path.basename(self.current_image_filename)))
            self.images.pop(self.image_index)
            if self.images:
                self.image_index %= len(self.images)
                self.show_image()
            else:
                self.canvas.delete("all")
                
    def label_3(self):
        if self.current_image:
            print("moving", self.current_image_filename, "to", os.path.join(self.folder_path, "3", os.path.basename(self.current_image_filename)))
            os.rename(self.current_image_filename, os.path.join(self.folder_path, "3", os.path.basename(self.current_image_filename)))
            self.images.pop(self.image_index)
            if self.images:
                self.image_index %= len(self.images)
                self.show_image()
            else:
                self.canvas.delete("all")
                
    def on_key_press(self, event):
        if event.char == "1":
            self.label_1()
        elif event.char == "2":
            self.label_2()
        elif event.char == "3":
            self.label_3()
                
root = tk.Tk()
app = Labeller(root)
root.mainloop()
