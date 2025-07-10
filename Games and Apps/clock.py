import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)

def toggle_fullscreen(event=None):
    root.attributes('-fullscreen', False)
    root.destroy()

root = tk.Tk()
root.title("Digital Clock")
root.attributes('-fullscreen', True)
root.configure(background='black')

label = tk.Label(root, font=("Arial", 120), bg="black", fg="cyan")
label.pack(expand=True, fill='both')

root.bind('<Escape>', toggle_fullscreen)

update_time()
root.mainloop()
