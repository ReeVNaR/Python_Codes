import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import numpy as np
from sklearn.cluster import KMeans

class ColorPaletteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎨 AI Color Palette Generator")
        self.root.geometry("720x720")
        self.root.configure(bg="#ffffff")

        # Title
        self.title = tk.Label(
            root, text="🎨 Import an image to extract its color palette",
            font=("Segoe UI", 18, "bold"), bg="#ffffff", fg="#333333"
        )
        self.title.pack(pady=20)

        # Import Button
        self.import_btn = tk.Button(
            root, text="📁 Import Image", command=self.import_image,
            font=("Segoe UI", 14), bg="#0066cc", fg="white",
            activebackground="#005bb5", activeforeground="white",
            relief="flat", padx=20, pady=10, cursor="hand2"
        )
        self.import_btn.pack(pady=10)

        # Image Preview
        self.image_label = tk.Label(root, bg="#ffffff")
        self.image_label.pack(pady=10)

        # Palette Frame
        self.palette_frame = tk.Frame(root, bg="#ffffff")
        self.palette_frame.pack(pady=10)

        # Save Button
        self.save_btn = tk.Button(
            root, text="💾 Save Palette as Image", command=self.save_palette,
            font=("Segoe UI", 12), bg="#28a745", fg="white",
            activebackground="#218838", activeforeground="white",
            relief="flat", padx=15, pady=8, cursor="hand2"
        )
        self.save_btn.pack(pady=20)

        self.current_colors = []

    def import_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
        )
        if not file_path:
            return

        img = Image.open(file_path).convert("RGB")
        img.thumbnail((300, 300))
        tk_img = ImageTk.PhotoImage(img)
        self.image_label.configure(image=tk_img)
        self.image_label.image = tk_img

        self.current_colors = self.get_palette(file_path)
        self.display_palette(self.current_colors)

    def get_palette(self, image_path, num_colors=5):
        image = Image.open(image_path).convert("RGB").resize((200, 200))
        data = np.array(image).reshape((-1, 3))
        kmeans = KMeans(n_clusters=num_colors, random_state=42, n_init='auto').fit(data)
        return [tuple(map(int, color)) for color in kmeans.cluster_centers_]

    def display_palette(self, colors):
        for widget in self.palette_frame.winfo_children():
            widget.destroy()

        for color in colors:
            hex_code = "#{:02x}{:02x}{:02x}".format(*color)

            frame = tk.Frame(self.palette_frame, bg="#ffffff")
            frame.pack(side=tk.LEFT, padx=10)

            swatch = tk.Label(
                frame, bg=hex_code, width=6, height=3,
                relief="ridge", bd=2, cursor="hand2"
            )
            swatch.pack()
            swatch.bind("<Button-1>", lambda e, code=hex_code: self.copy_to_clipboard(code))

            label = tk.Label(
                frame, text=hex_code, font=("Courier New", 10),
                bg="#ffffff", fg="#333333"
            )
            label.pack(pady=5)

    def copy_to_clipboard(self, hex_code):
        self.root.clipboard_clear()
        self.root.clipboard_append(hex_code)
        self.root.update()
        messagebox.showinfo("Copied!", f"{hex_code} copied to clipboard!")

    def save_palette(self):
        if not isinstance(self.current_colors, list) or len(self.current_colors) == 0:
            messagebox.showwarning("No palette", "Please import an image first.")
            return

        img_width = 100 * len(self.current_colors)
        img = Image.new("RGB", (img_width, 100), "white")
        draw = ImageDraw.Draw(img)

        try:
            font = ImageFont.truetype("arial.ttf", 16)
        except:
            font = ImageFont.load_default()

        for i, color in enumerate(self.current_colors):
            hex_code = "#{:02x}{:02x}{:02x}".format(*color)
            x0 = i * 100
            draw.rectangle([x0, 0, x0 + 100, 100], fill=hex_code)
            draw.text((x0 + 10, 70), hex_code, fill="black", font=font)

        save_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png")],
            title="Save Palette Image"
        )

        if save_path:
            img.save(save_path)
            messagebox.showinfo("Saved", f"Palette saved to:\n{save_path}")

# Launch
if __name__ == "__main__":
    root = tk.Tk()
    app = ColorPaletteApp(root)
    root.mainloop()