import tkinter as tk
from tkinter import ttk


def greet():
    user_name.set("ok")


root = tk.Tk()
root.title('myapp')
user_name = tk.StringVar()
# my_label = tk.Label(root, text="Hello every body", padx=40,
#                     pady=40, background="cyan", font=15)
my_label = ttk.Label(root, text="Hello every body",
                     padding=(10, 10), background="cyan", font=15, textvariable=user_name)
my_label.pack(fill="x")
greet_button = ttk.Button(root, text="Greet", padding=(
    10, 10), width=50, command=greet)
greet_button.pack(side="left", fill="both", expand=True)
quit_button = ttk.Button(root, text="Quit", padding=(
    10, 10), width=50, command=root.destroy)
quit_button.pack(side="left", fill="both", expand=True)
root.mainloop()
