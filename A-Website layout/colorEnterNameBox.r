import tkinter as tk
from tkinter import messagebox

def change_color():
    color = color_entry.get()  
    try:
        color_box.config(bg=color)  .
    except tk.TclError:
        messagebox.showerror("Invalid Color", f"'{color}' is not a valid color code or name")
root = tk.Tk()
root.title("Color Box")
color_box = tk.Frame(root, width=200, height=100, bg="white")
color_box.pack(pady=10)
color_entry = tk.Entry(root, width=20)
color_entry.pack(pady=5)
apply_button = tk.Button(root, text="Apply Color", command=change_color)
apply_button.pack(pady=5)
root.mainloop()
