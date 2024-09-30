import tkinter as tk
from tkinter import messagebox
import random

def check_baby():
    conditions = ["Baby is sleeping well", "Baby is crying", "Baby is too hot", "Baby is moving a lot", "Baby's vitals are stable"]
    condition = random.choice(conditions)

    chatbox.insert(tk.END, f"Monitor: {condition}\n")

    if "crying" in condition:
        messagebox.showwarning("Alert", "Baby is crying! Please check.")
    elif "too hot" in condition:
        messagebox.showwarning("Alert", "Baby is too hot! Check the room temperature.")
    elif "moving" in condition:
        messagebox.showwarning("Alert", "Baby is moving a lot! Check if everything is alright.")
    else:
        chatbox.insert(tk.END, "No issues detected.\n")

def monitor_baby():
    check_baby()
    root.after(5000, monitor_baby)  
root = tk.Tk()
root.title("Baby Monitor")
root.geometry("400x400")
root.configure(bg="lightblue")

chatbox = tk.Text(root, height=15, width=40)
chatbox.pack(pady=10)
start_button = tk.Button(root, text="Start Monitoring", command=monitor_baby)
start_button.pack(pady=10)
root.mainloop()
