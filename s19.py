import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

frame_1 = ttk.Frame(root)
frame_1.grid(row=0, column=0, sticky="ew")

frame_1.columnconfigure(0, weight=1)
frame_1.columnconfigure(1, weight=1)

name_label = ttk.Label(frame_1, text="name: ")
name_label.grid(row=0, column=0, sticky="ew")

name_entry = ttk.Entry(frame_1)
name_entry.grid(row=0, column=1, sticky="ew")


# frame_2 = ttk.Frame(root)
# frame_2.grid(row=1, column=0)

# family_label = ttk.Label(frame_2, text="family: ")
# family_label.grid(row=0, column=0)

# family_entry = ttk.Entry(frame_2)
# family_entry.grid(row=0, column=1)

root.mainloop()
