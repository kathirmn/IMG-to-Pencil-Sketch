import cv2
import tkinter as tk
from tkinter import filedialog, simpledialog, ttk, messagebox

class PencilSketchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pencil Sketch App")

        self.input_image = None
        self.output_image = None

        self.sigma_s = tk.DoubleVar(value=80)
        self.sigma_r = tk.DoubleVar(value=0.15)
        self.shade_factor = tk.DoubleVar(value=0.06)

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Select an Image").pack(pady=10)
        ttk.Button(self.root, text="Browse", command=self.open_file_dialog).pack()
        ttk.Label(self.root, text="Parameter Values (leave blank to use defaults)").pack(pady=10)
        ttk.Label(self.root, text="Sigma_s:").pack()
        ttk.Entry(self.root, textvariable=self.sigma_s).pack()
        ttk.Label(self.root, text="Sigma_r:").pack()
        ttk.Entry(self.root, textvariable=self.sigma_r).pack()
        ttk.Label(self.root, text="Shade Factor:").pack()
        ttk.Entry(self.root, textvariable=self.shade_factor).pack()
        ttk.Button(self.root, text="Generate Sketch", command=self.generate_sketch).pack(pady=10)

    def open_file_dialog(self):
        self.input_image = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tiff *.ppm *.pgm")])

    def generate_sketch(self):
        if not self.input_image:
            messagebox.showwarning("Warning", "Please select an image.")
            return

        
        sigma_s = self.sigma_s.get()
        sigma_r = self.sigma_r.get()
        shade_factor = self.shade_factor.get()

        if not sigma_s:
            sigma_s = 80
        if not sigma_r:
            sigma_r = 0.15
        if not shade_factor:
            shade_factor = 0.06

        output_image = simpledialog.askstring("Input", "Enter output file name (e.g., output.jpg):")
        if not output_image:
            return

        
        if not output_image.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".ppm", ".pgm")):
            output_image += ".jpg"  

        image = cv2.imread(self.input_image)

        
        sketch, _ = cv2.pencilSketch(image, sigma_s=sigma_s, sigma_r=sigma_r, shade_factor=shade_factor)

        cv2.imwrite(output_image, sketch)
        messagebox.showinfo("Success", f"Pencil sketch saved as {output_image}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PencilSketchApp(root)
    root.mainloop()
